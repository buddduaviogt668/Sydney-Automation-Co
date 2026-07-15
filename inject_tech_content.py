import glob, re

# Content database: device-specific troubleshooting per issue type
# Format: model -> issue_type -> {direct_answer, steps}
CONTENT = {
    "5500PC": {
        "blinking-led-codes": {
            "answer": "The 5500PC unit LED blinking 3 times then pausing indicates a failed network clock or the USB-to-serial adapter not being recognised. On the 5500PC USB variant, the green C-Bus LED should be solid when connected to active C-Bus network. If blinking, measure 15-36V DC across C-Bus + and - on the RJ45. If voltage is good but LED blinks, check the FTDI USB driver — C-Bus Toolkit 1.16.4+ does NOT support Prolific chipsets.",
            "steps": [
                "Measure DC voltage across C-Bus + and - terminals on the 5500PC RJ45. Acceptable range: 15-36V DC. Below 15V indicates a failed power supply module.",
                "Open Device Manager > Ports (COM & LPT). The 5500PCU should appear as 'C-Bus Wired PC Interface (5500PCU)'. If using a Prolific-based USB adapter, swap to FTDI-based adapter (FT232R, US232R-10).",
                "Close C-Gate console via the 'SHUTDOWN' command, restart Toolkit fresh. Ensure USB adapter is plugged in BEFORE launching C-Gate.",
                "In Toolkit, open Network > Unit Dialog. Verify 'Network Burden' is enabled and the unit is set to Unit 001 if it provides the system clock.",
                "If the 5500PC still does not connect, try a full power cycle: disconnect both USB and C-Bus for 2 minutes, then reconnect USB first, wait 30 seconds, then connect C-Bus."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "A buzzing or clicking 5500PC is almost always the internal relay (on older 5500PCI variants) or the USB-Serial adapter producing audible coil noise. The 5500PC has no moving parts except the optional relay for override. If the noise is coming from the C-Bus network side, check the 5500PS power supply unit — a failing PSU transformer can produce audible 50Hz hum. If the 5500PC clicks repeatedly, it may be the internal C-Bus transceiver resetting in a watchdog loop.",
            "steps": [
                "Isolate the noise source: disconnect the USB cable. If the clicking stops, the issue is on the PC side (driver conflict, COM port polling). If it continues, the noise is on the C-Bus side.",
                "If the noise is a 50Hz hum, measure the C-Bus voltage. A buzzing power supply typically outputs noisy DC with >1V ripple. Use a multimeter in AC mode across C-Bus + and - — should read <100mV AC ripple.",
                "For clicking relays, the 5500PC's optional relay module (if fitted) may have welded contacts. Disconnect all C-Bus wiring and check resistance across the relay terminals.",
                "Replace the C-Bus power supply (5500PS) if the ripple voltage exceeds 500mV AC."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "The 5500PC appears 'frozen' when C-Bus Toolkit cannot discover it on any COM port despite the green power LED being on. This is typically caused by the C-Gate console holding the COM port open from a previous crash. Killing the C-Gate process via Task Manager and restarting usually resolves it. Alternatively, the FTDI chipset may have entered 'deep sleep' mode — unplugging and replugging the USB cable resets it.",
            "steps": [
                "Open Task Manager > Processes and end 'C-Gate.exe' or 'java.exe' (C-Gate runs on Java). Restart Toolkit fresh.",
                "If that fails, unplug the USB cable, wait 10 seconds, and reconnect. Windows will re-enumerate the device.",
                "Check Device Manager for the COM port number. Toolkit defaults to COM1 if it cannot find the assigned port. Manually set the COM port in Toolkit > Options > Set Default Interface.",
                "If using a 5500PCI (serial RS232), ensure the USB-to-serial adapter is FTDI-based. Toolkit 1.12+ does NOT support Prolific PL2303 adapters.",
                "Last resort: reboot the PC. The 5500PCU itself rarely fails — 95% of 'frozen' issues are PC-side."
            ]
        },
        "lost-schedules-and-clock-drift": {
            "answer": "The 5500PC does not store schedules — it is a PC interface only. Lost schedules point to the device providing the network clock (usually a touch screen or another controller) having lost its timekeeping battery. On a C-Bus network, the clock driver is a unit configured with 'Network Clock' enabled. If that unit's internal CR2032 battery has died (typical lifespan 5-7 years), the clock resets to 1-Jan-2000 on every power cycle, causing schedule drift.",
            "steps": [
                "Identify which unit on the network is configured as the 'Network Clock' driver. In Toolkit, go to Network > Properties > Clock Auto-Configure.",
                "Check the date/time on all touch screens and controllers. If any shows 1-Jan-2000, its internal battery (CR2032) has failed.",
                "Replace the CR2032 coin cell battery on the affected unit. Settings are retained in EEPROM but the real-time clock loses power.",
                "After battery replacement, reconfigure the clock via Toolkit or the touch screen's date/time settings menu.",
                "If clock drift is consistent (e.g. loses 5 minutes per day), the 32.768kHz crystal oscillator on the clock source unit is failing and the unit needs replacement."
            ]
        },
        "stuck-on-channels": {
            "answer": "The 5500PC has no output channels — it is a PC interface only. If a C-Bus channel appears stuck on or off, it is the relay or dimmer module controlling that circuit, not the 5500PC. The 5500PC is correctly reporting the network status. Use Toolkit to identify which unit address controls the stuck channel and diagnose that unit directly.",
            "steps": [
                "Use Toolkit's Network Diagnostic utility to identify the unit address controlling the stuck channel.",
                "Navigate to that unit (e.g. relay module L5512RVF or dimmer L5508D1A) via Network > Unit Dialog.",
                "Perform a unit-level test: toggle the specific channel ON and OFF from the Unit Dialog while listening for the relay click.",
                "If the unit responds to Toolkit commands but the physical channel does not switch, the output device has a hardware fault (welded relay, failed triac).",
                "The 5500PC itself is functioning correctly — it is a diagnostic tool, not the cause of the stuck channel."
            ]
        },
        "surge-storm-damage": {
            "answer": "A 5500PC that has suffered an electrical surge typically shows no LEDs at all or a permanently dim C-Bus LED. The 5500PCU (USB variant) has limited surge protection — the USB port is vulnerable to ground potential differences between the PC and the C-Bus network. In commercial buildings, the PC earth and C-Bus earth can have several volts of potential difference, causing current to flow through the USB shield and damaging the FTDI chipset.",
            "steps": [
                "Check if the 5500PC shows any LED activity when powered. If no LEDs at all, the internal 5V regulator has likely failed. Test by measuring 5V DC across test points on the PCB.",
                "If the C-Bus LED is very dim, the unit is receiving insufficient power. Measure C-Bus voltage at the 5500PC's RJ45 — should be 15-36V DC.",
                "Inspect for visible surge damage: bulging capacitors, charred components near the USB connector, or a burnt smell from the FTDI chip.",
                "The 5500PCU is an economic replacement vs repair (approximately $200-300 AUD). Replace rather than attempting component-level repair of surge-damaged boards.",
                "For future protection, install a C-Bus surge arrestor (part number: 5500SA) on the network to protect all C-Bus devices from mains-borne surges."
            ]
        }
    },
    "5500CN": {
        "blinking-led-codes": {
            "answer": "The 5500CN has three status LEDs: Power, C-Bus, and Ethernet. If the Ethernet LED shows a solid green link with no cable connected, the internal Lantronix XPort is running on undervoltage. Measure the DC input: should be 9-12V AC or DC at minimum 500mA. Below 7.5V, the XPort will show false link status. The 5500CN is effectively a 5500PCI with a Lantronix MSS100 serial-to-Ethernet converter bolted inside.",
            "steps": [
                "Measure the PSU output voltage under load. The 5500CN needs 9-12V DC or AC at minimum 500mA. If below 7.5V, replace the PSU (Mean Well RS-15-12 is a direct drop-in replacement).",
                "If the Ethernet LED shows green with no cable, test with a known-good 12V 1A supply directly into the power terminals. If the LED turns red, the original internal regulator was failing.",
                "For network discovery issues, use the ARP spoofing method: 'arp -s <temp_ip> <mac_address>' with a direct crossover cable, then telnet to port 1.",
                "Disconnect the C-Bus pink cables. If the C-Bus LED stays off with only the PSU connected, the internal C-Bus transceiver or power regulator has failed."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "The 5500CN has no moving parts or audible indicators — a buzzing noise from the unit indicates the internal PSU transformer is failing. The 5500CN uses a small switch-mode PSU module that can produce audible high-frequency whine when the electrolytic capacitors are drying out. This is a known failure mode on units over 5 years old, as the internal capacitors age from the constant heat inside the enclosure.",
            "steps": [
                "Listen carefully to identify the noise source. A high-frequency whine (>10kHz) is the PSU switching transistor oscillating at the wrong frequency due to failing capacitors.",
                "Measure the DC output of the internal PSU under load. If the voltage fluctuates by more than 0.5V, the primary-side electrolytic capacitor (typically 47µF 400V) needs replacement.",
                "Replace the internal PSU module or the entire 5500CN. The newer 5500CN2 has a redesigned PSU with extended life capacitors.",
                "If the buzzing is accompanied by intermittent network dropouts, replace the unit immediately — failing PSUs can take other C-Bus devices offline when they fail short."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "A 5500CN that is powered (LEDs on) but unresponsive to network pings or telnet usually has a crashed Lantronix XPort module. The XPort runs an embedded Linux OS and can freeze after extended uptime (months/years). A full power cycle (disconnect both C-Bus and PSU for 30 seconds) typically restores function. If the freeze occurs weekly, the XPort firmware may be corrupted.",
            "steps": [
                "Power-cycle the 5500CN: disconnect both the 9-12V PSU and the C-Bus pink cables for at least 30 seconds.",
                "After reboot, try pinging the 5500CN's IP address. If it responds, telnet to port 9999 and issue the 'reboot' command to force a clean restart.",
                "If the unit still does not respond, use the Lantronix DeviceInstaller software to scan the local subnet for the 5500CN's MAC address.",
                "As a last resort, perform a factory reset: hold the reset button (small hole on the front panel) for 10 seconds while applying power.",
                "If none of the above works, the XPort module or the internal 5500PCI daughterboard has failed. Replace with a 5500CN2 (current model)."
            ]
        },
        "surge-storm-damage": {
            "answer": "The 5500CN is highly vulnerable to surge damage because the Ethernet port provides a direct path for ground potential differences between building floors. The internal Lantronix XPort has only basic ESD protection on the RJ45. A common failure after storm activity is the Ethernet PHY chip failing — the 5500CN powers up but the Ethernet LED stays off. The C-Bus side usually survives because the 5500PCI parallel board has its own isolation.",
            "steps": [
                "After a storm, check the 5500CN's power LED. If off, the internal PSU has failed. If on but Ethernet LED off, the XPort or Ethernet PHY has been damaged.",
                "Disconnect the Ethernet cable and test with a known-good laptop directly via crossover cable. If still no link, the XPort module is damaged.",
                "Check the 5500PCI board inside the 5500CN enclosure. It is a standard 5500PCI that can be tested independently with a USB-to-serial adapter.",
                "The 5500CN2 has improved Ethernet surge protection compared to the original 5500CN.",
                "To protect the entire C-Bus network from future surges, install a 5500SA surge arrestor at the network's electrical entry point."
            ]
        },
        "lost-schedules-and-clock-drift": {
            "answer": "Like the 5500PC, the 5500CN itself does not store schedules. Lost schedules across the C-Bus network suggest the designated Clock Driver unit has lost time. The 5500CN can be configured as a network clock driver via Toolkit, and if so, its internal RTC battery (CR2032) failing would cause all network schedules to drift or fail.",
            "steps": [
                "Check if the 5500CN is configured as the Network Clock: Runtime > Network > Properties > Clock Auto-Configure.",
                "If the 5500CN is the clock source, check its internal battery. The 5500CN uses a CR2032 on the 5500PCI daughterboard.",
                "Replace the CR2032 battery if the date shows pre-2000 after a power cycle.",
                "If clock drift is gradual (minutes per week), the 32.768kHz crystal may be failing due to aging or previous surge damage."
            ]
        }
    },
    "L5508D1A": {
        "blinking-led-codes": {
            "answer": "The L5508D1A dimmer has a green status LED per channel that blinks when the triac has failed short-circuit. A channel LED blinking rapidly (4-5 times per second) indicates the internal triac (ST T1620-600W) has failed closed — the channel will be stuck ON at full brightness regardless of C-Bus commands. If the Unit LED blinks in a pattern of 3 flashes-pause-repeating, the internal C-Bus transceiver has lost communication with the microcontroller.",
            "steps": [
                "For a channel stuck ON, isolate the load and measure DC resistance across the triac (A1-A2) with power OFF. A shorted triac reads <5 ohms. Replace triac (ST T1620-600W or equivalent BTA16-600SW).",
                "For the 3-flash-pause unit failure, disconnect C-Bus and reapply power. If the pattern persists, the microcontroller has crashed and needs a full 30-minute power removal to reset.",
                "Test the internal C-Bus power supply by disconnecting from the network. If the C-Bus LED stays lit after removing the PCI, the internal PSU cap is failing.",
                "Measure C-Bus + to Earth and - to Earth — should be within 1V of each other. >2V difference indicates a ground fault in the field wiring."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "An L5508D1A producing an audible buzz is a classic sign of a failing triac or a failed snubber circuit. The snubber (RC network across the triac) suppresses the high-frequency ringing when the triac switches off. When the snubber capacitor dries out, the triac switches with a 'snap' that produces audible noise. If the noise is a 50Hz hum, it is likely a failing PSU capacitor causing magnetic vibration in the internal transformer.",
            "steps": [
                "Identify which channel is buzzing by switching each channel OFF and ON in sequence. The buzzing channel will stop when OFF.",
                "Check for loose wiring connections. Tighten all terminal screws — loose connections can cause arcing that sounds like buzzing.",
                "Measure the load being controlled. If the load exceeds 1200W for incandescent or 400W for LED, the triac may be operating beyond its safe thermal limits.",
                "If the snubber has failed, replace the dimmer module. Internal snubber repair is possible but requires desoldering the RC network from the main PCB.",
                "For persistent buzzing on multiple channels, replace with the L5508D2U universal dimmer which has improved snubber circuitry."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "An L5508D1A that is powered (Unit LED on) but unresponsive to Toolkit or local button presses has experienced a microcontroller lockup. The dimmer's PIC microcontroller can freeze due to electrical noise on the C-Bus network or a mains-borne transient. A full power cycle (remove 240V AND C-Bus for 2 minutes) resets the microcontroller. If the freeze recurs weekly, the internal crystal oscillator (typically 4MHz or 10MHz) may be failing.",
            "steps": [
                "Remove both 240V supply and C-Bus connection for at least 2 minutes to fully discharge all capacitors.",
                "Reconnect C-Bus first, then 240V. The unit should boot with a solid Unit LED.",
                "In Toolkit, navigate to the unit's dialog and attempt to read its firmware version. If it responds, the microcontroller has recovered.",
                "If the unit freezes again within 24 hours, the internal crystal oscillator or the PIC microcontroller itself is failing. Replace the dimmer."
            ]
        },
        "lost-schedules-and-clock-drift": {
            "answer": "The L5508D1A dimmer does not store schedules independently — it is a controlled device, not a controller. Lost schedules affecting dimmer channels point to the Clock Driver unit (usually a touch screen or 5500CN) that provides the network clock having a failed battery. The dimmer simply responds to the commands it receives; if the correct commands are not being sent, the clock source is at fault.",
            "steps": [
                "Check the Clock Driver unit on the network via Toolkit: Network > Properties > Clock Auto-Configure.",
                "Verify all touch screens and controllers show the correct date and time. A CR2032 battery replacement may be needed on the clock source.",
                "If the dimmer loses its group address bindings after a power cycle, the internal EEPROM may be corrupt. Re-upload the project database.",
                "Scheduled events are stored in the Clock Driver, not in the dimmer. Diagnose the controller unit for schedule issues."
            ]
        },
        "stuck-on-channels": {
            "answer": "A channel stuck ON on the L5508D1A is the most common dimmer failure — the T1620-600W triac has failed short-circuit from end-of-life lamp arcing or LED driver inrush current. The channel LED stays solid orange regardless of C-Bus commands. If multiple channels are stuck simultaneously, the internal 5V microcontroller supply has failed, causing all triac gate drivers to float high.",
            "steps": [
                "Isolate the affected channel: disconnect the load wire and measure DC resistance across the triac (A1-A2) with unit powered OFF. <5 ohms confirms shorted triac.",
                "Check if the dimmer's internal 5V rail is present. Measure across the 5V test point and GND on the PCB — should be 4.75-5.25V DC.",
                "If a single channel is stuck, the triac can be replaced (ST T1620-600W or BTA16-600SW). For multiple channels, the microcontroller or 5V regulator (LM2575) has failed.",
                "After triac replacement, test with a small resistive load (60W incandescent globe) before reconnecting the full LED load.",
                "Install a 31LCDA load correction device across the channel to protect the new triac from LED capacitive inrush."
            ]
        },
        "surge-storm-damage": {
            "answer": "The L5508D1A is vulnerable to mains-borne surges because the 240V supply connects directly to the triac anodes and internal PSU. After a lightning storm, multiple channels failing simultaneously indicates the common-mode surge has damaged the microcontroller or 5V regulator. The internal MOV (Metal Oxide Varistor) across the mains input may have sacrificed itself — if the MOV has exploded or cracked, the unit may still work but has no overvoltage protection.",
            "steps": [
                "Inspect the dimmer for visible surge damage: bulging or leaking capacitors, charred MOV, cracked PCB tracks near the mains input.",
                "Test each channel independently with a known-good incandescent test load. Note which channels are completely dead vs stuck vs functional.",
                "If all channels are dead but the Unit LED is on, the microcontroller has been damaged. The unit needs replacement.",
                "If only some channels are damaged, the triacs can be individually replaced. Inspect the gate driver resistors for each channel.",
                "Install a 5500SA surge arrestor on the C-Bus network to protect all dimmers from future mains-borne surges."
            ]
        }
    },
    "L5508D2A": {
        "blinking-led-codes": {
            "answer": "Same triac short indicator as the L5508D1A but the D2A variant uses leading-edge phase control only, making it incompatible with many LED drivers. A channel LED blinking rapidly on the D2A often indicates the dimmer has detected a load fault (capacitive load exceeding 300nF). This is not a hardware failure but a load compatibility issue — the D2A should be replaced with the L5508D2U universal dimmer for LED installations.",
            "steps": [
                "If the channel blinks but is not stuck ON, disconnect the LED load and test with an incandescent globe. If it works with incandescent, the LED driver is incompatible.",
                "Measure the total input capacitance of the connected LED drivers with an LCR meter across the load terminals (unit powered off). Sum must be <300nF per channel.",
                "Install a 31LCDA load correction device if the total capacitance exceeds 300nF. This adds inductive compensation to stabilise the dimmer.",
                "If multiple channels show the same issue, replace the D2A with a D2U (universal dimmer) that supports both leading and trailing edge modes."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "The L5508D2A buzzes audibly when used with electronic transformers or LED drivers that have high input capacitance. The leading-edge triac fires asymmetrically when driving capacitive loads, creating a DC offset that causes the connected transformer's core to saturate and buzz. This buzz is actually coming from the load, not the dimmer itself, but it indicates the dimmer is being forced outside its design parameters.",
            "steps": [
                "Swap the buzzing load to a channel known to work quietly. If the buzz moves with the load, the load is incompatible. If the buzz stays on the channel, the triac is failing.",
                "Replace the D2A dimmer with the D2U universal dimmer which auto-selects leading or trailing edge for optimal load matching.",
                "If immediate replacement is not possible, install a 31LCDA load correction device on the buzzing channel.",
                "Reduce the minimum dim level in Toolkit to 20% — dimming below 20% on leading-edge dimmers increases audible noise."
            ]
        },
        "stuck-on-channels": {
            "answer": "Triac failure on the L5508D2A presents identically to the D1A — the channel stays ON at full brightness. However, the D2A is more prone to this with LED loads because the leading-edge control method subjects the triac to higher di/dt stress at switch-on. The recommended fix is to upgrade to the D2U universal dimmer which uses trailing-edge for LED loads, significantly reducing triac stress.",
            "steps": [
                "Isolate the stuck channel and verify the triac has failed short (measure <5 ohms across A1-A2).",
                "Replace the stuck channel's triac (BTA16-600SW or equivalent) OR swap to D2U universal dimmer.",
                "If the D2A was installed within the last 5 years, check if it is still under warranty with Clipsal/Schneider Electric.",
                "For new installations, always specify the L5508D2U universal dimmer instead of the L5508D2A for LED compatibility."
            ]
        }
    },
    "L5512RVF": {
        "blinking-led-codes": {
            "answer": "The L5512RVF relay module blinks its Unit LED in a 3-flash pattern when the internal C-Bus power supply is failing. The 12V DC rail from the internal switch-mode PSU has dropped below the microcontroller's brownout threshold (typically 4.5V for the 5V rail). The relay will still switch because the latching relays hold their state, but the unit cannot receive new C-Bus commands. The internal 1A 250V ceramic SMD fuse near the mains input may also have blown from a surge.",
            "steps": [
                "Measure 240V across A/L and N terminals. If present but Unit LED is off, check the small SMD fuse near the mains input (usually 1A 250V ceramic).",
                "If the Unit LED blinks 3 times repeatedly, the internal 5V regulator (LM2575 or similar) has failed. Replace the regulator IC or the entire module.",
                "Check the C-Bus voltage on the pink RJ45. The L5512RVF provides ~20mA to the network; if the unit fails, the C-Bus voltage may dip.",
                "Test the unit in isolation with only a 5500PC and a burden. If the blinking persists without any C-Bus load, the internal PSU is the root cause."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "Buzzing from an L5512RVF is almost always one of the latching relays oscillating between open and closed. Latching relays hold their position magnetically and require a pulsed current to switch. If the relay coil driver chip (ULN2003) has failed, it may send multiple switch pulses, causing the relay to chatter. A continuous 50Hz hum indicates the internal PSU transformer laminations are vibrating loose — a sign of imminent PSU failure.",
            "steps": [
                "Identify which relay is chattering by cycling each channel ON and OFF. The noisy relay will sound different when switching.",
                "If a relay chatters continuously, remove power and measure the resistance of that relay's coil. Should read 200-400 ohms. Open coil = <10 ohms or >1K ohm.",
                "If the ULN2003 coil driver IC has failed, replace the IC (SOIC-16 package) or the entire relay module.",
                "For transformer hum, remove the enclosure cover and apply gentle pressure to the PSU transformer. If the hum changes, the laminations are loose and the PSU needs replacement."
            ]
        },
        "stuck-on-channels": {
            "answer": "A relay stuck ON on the L5512RVF is caused by welded relay contacts. C-Bus latching relays use a permanent magnet to hold state without power, and the contacts can weld shut if the switched current exceeds the 20A rated maximum — particularly with capacitive LED driver inrush. A single loud 'clunk' when the relay tries to switch but cannot release confirms welded contacts. The affected relay must be replaced.",
            "steps": [
                "With power OFF, measure resistance across each relay output (1A-1B etc). A normally-open contact that reads <1 ohm is welded shut.",
                "Check the remote override terminals on the RJ45 — moisture or a stray wire strand shorting the override pins overrides all channels ON.",
                "If the relay is stuck mechanically, a sharp tap with a screwdriver handle sometimes frees it temporarily, but replacement is the only permanent fix.",
                "Inspect the load circuit for high inrush devices. LED driver banks with 50+ drivers can exceed 200A inrush for microseconds — install soft-start or inrush limiters."
            ]
        },
        "surge-storm-damage": {
            "answer": "After a lightning storm, an L5512RVF with multiple stuck relays and a blown Unit LED indicates a catastrophic surge failure. The 240V mains has coupled through the switch-mode PSU and directly into the 5V microcontroller rail, destroying the main processor. The C-Bus transceiver (SN75176 or similar) is also likely damaged. These units are rarely economic to repair — replacement is standard.",
            "steps": [
                "Disconnect power immediately. Inspect for visible damage: bulging capacitors, cracked PCB, burnt smell around the PSU section.",
                "Test all 12 relay outputs for contact welding. Surge-damaged units often have 4-8 relays welded simultaneously.",
                "Replace the entire L5512RVF module. The 'P' suffix variant (L5512RVFP) is the current replacement.",
                "Install a 5500SA surge arrestor on the C-Bus network and a mains-rated surge protector (Type 2) on the distribution board supplying the unit."
            ]
        }
    },
    "5508RVF": {
        "blinking-led-codes": {
            "answer": "The 5508RVF has a unique failure mode where both C-Bus and Unit LEDs flash alternately approximately 6-7 times then pause — indicating the microcontroller is stuck in a watchdog reset loop. This typically follows a mains brownout or surge. The watchdog timer keeps resetting the microcontroller before it can boot, creating the alternating flash pattern. Even with no C-Bus cables connected, the flashing continues.",
            "steps": [
                "Isolate the unit from the C-Bus network entirely. Connect only a 5500PC and a 5500PS. If the alternating flash continues, the microcontroller has crashed.",
                "Remove ALL power (240V AND C-Bus) for at least 30 minutes to fully discharge all electrolytic capacitors.",
                "After reconnection, if the pattern continues, the internal 5V rail regulator (LM2575) may be outputting noisy voltage. Replace the regulator.",
                "If no change, the internal EEPROM (24LC512) has corrupted boot parameters. The unit is beyond field repair and needs replacement."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "The 5508RVF uses the same latching relays as the L5512RVF and the same buzzing/chattering failure modes apply. Additionally, the 5508RVF has a known issue where the main power relay (internal, not the output channels) can chatter when the internal 12V rail is below 10V. This sounds like a rapid clicking from inside the enclosure.",
            "steps": [
                "Measure the 12V DC rail on the PCB (between the LM2575 output cap and ground). If below 11V, the PSU regulator is failing.",
                "Identify the chattering relay by listening to each output channel in sequence.",
                "Replace the PSU section (LM2575 + 100µF output capacitor) if the 12V rail is noisy."
            ]
        },
        "stuck-on-channels": {
            "answer": "Same latching relay weld failure as L5512RVF. The 5508RVF switches 8 channels at 20A each. The high-inrush problem is worse on this unit because it is often used in lighting distribution boards where long cable runs create additional capacitive inrush. A 3-phase configuration can cause neutral shift that doubles the switching voltage across the relay contacts, accelerating weld failures.",
            "steps": [
                "Disconnect all loads and test each relay for contact welding (resistance <1 ohm when open).",
                "The internal relays are standard 12V latching relays (SRD-12VDC-SL-C or equivalent). They can be individually desoldered and replaced.",
                "Check the 3-phase wiring configuration — the 5508RVF must have Channel 1 on the same phase as the control supply for correct zero-cross switching."
            ]
        }
    },
    "5502DAL": {
        "blinking-led-codes": {
            "answer": "All three LEDs (Install, Id, Manual) flashing red rapidly indicates CRITICAL — mains voltage has been applied to the DALI line. The 5502DAL detects this and immediately shuts down the DALI bus, retrying every 15 seconds. Solid yellow on the Install LED indicates a DALI line fault (short circuit, open circuit, or loss of DALI bus power). The DALI bus should measure 16V DC across DA+ and DA-.",
            "steps": [
                "If all 3 LEDs flash red, isolate power to the 5502DAL and all DALI devices immediately. Check for mains voltage (>50V AC) between DA+ and DA- using a multimeter.",
                "If Install LED is solid yellow, press the Install button briefly to refresh DALI line status. Measure DC voltage across DA+ and DA- — should be 16V DC. Below 10V indicates a short or overload.",
                "Use the service switch: 3 presses in 4 seconds drives all ballasts to 100%. 4 presses runs the DALI dim test sequence (0%-50%-100% cycling every 5 seconds for 5 minutes).",
                "If a specific DALI line fails the test, disconnect drivers one at a time until the line recovers. The faulty driver has a shorted input."
            ]
        },
        "buzzing-or-clicking-noises": {
            "answer": "The 5502DAL has no moving parts or audible indicators. Any buzzing noise coming from the 5502DAL enclosure is actually the external DALI bus PSU or a nearby relay module. The gateway itself consumes under 2W and runs cool. If the buzzing is from the DALI bus, it is likely one of the connected DALI drivers — not the gateway.",
            "steps": [
                "Locate the actual source of the buzzing noise. It may be a nearby relay module sharing the same DIN rail.",
                "If a DALI driver is buzzing, it has a failing internal PSU. The driver needs replacement.",
                "If the 5502DAL's enclosure vibrates, tighten the DIN-rail mounting clips and ensure adjacent modules have a 10mm air gap for cooling."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "A 5502DAL appears 'frozen' when System Builder cannot discover its DALI devices. This is usually a DALI bus fault, not the gateway itself — the gateway has been designed to continue operating independently even if the DALI line short-circuits. A frozen 5502DAL where the LEDs are all off indicates the internal C-Bus power supply or the 24V external supply has failed.",
            "steps": [
                "Check the external 24V DC supply (if used). The 5502DAL can be powered from C-Bus (15-36V DC) or external 24V (22-28V DC).",
                "If C-Bus powered, measure the voltage at the 5502DAL's pink C-Bus input — should be 15-36V DC.",
                "If using external 24V, measure at the V+ and V- terminals. The 5502DAL draws 50mA from C-Bus or 30mA from external supply.",
                "Use the service switch to test the DALI bus independently of System Builder. The service switch functions work without any software connection."
            ]
        },
        "surge-storm-damage": {
            "answer": "The 5502DAL is designed to survive mains applied to the DALI bus (it detects and shuts down), but a lightning surge on the mains input can still damage the internal PSU. The self-resetting fuse on each DALI line can fail in a short-circuit condition after a severe surge, permanently shorting the DALI power supply. The gateway may still pass data but cannot power the DALI bus.",
            "steps": [
                "After a storm, check if the Install LED shows solid yellow (line fault). Measure the DALI bus voltage — should be 16V DC. If 0V, the DALI line PSU has failed.",
                "Disconnect all DALI drivers from both lines. If the voltage returns to 16V with no drivers, the fuse and PSU are intact and the fault is in one of the drivers.",
                "If voltage stays at 0V with no drivers, the internal DALI bus PSU or self-resetting fuse has failed. The 5502DAL needs replacement.",
                "Install a Type 2 surge protector on the mains supply feeding the 5502DAL and all DALI drivers."
            ]
        }
    },
    "L5504D2U": {
        "blinking-led-codes": {
            "answer": "The L5504D2U channel LED flashing indicates short-circuit cut-out protection has triggered. The universal dimmer's protection circuit has detected an overload or short on that channel and has latched it off. The channel remains latched until the local button is toggled OFF and ON or the C-Bus command is cycled. Repeated cut-outs indicate a load fault, not a dimmer fault.",
            "steps": [
                "Identify which channel is latched by cycling the channel OFF and ON via C-Bus. If it restores but trips again, the connected load has a fault.",
                "Disconnect the load and test the dimmer channel with a known-good incandescent globe. If it works, the LED driver or wiring is at fault.",
                "Measure the total capacitance of the connected LED drivers — must be <300nF per channel. If exceeded, install a 31LCDA.",
                "Check wiring for short circuits using an insulation resistance tester between Active and Neutral — should be >1M ohm.",
                "The D2U uses auto-detecting leading/trailing edge. Confirm the correct mode is selected for the connected load type."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "A frozen L5504D2U where channels do not respond to commands but the Unit LED is on usually points to a corrupted group address binding. The dimmer's internal EEPROM may have lost its configuration from a power failure during commissioning. Re-uploading the project database via Toolkit typically restores function.",
            "steps": [
                "In Toolkit, navigate to the L5504D2U's unit dialog and check if it responds. If yes, re-upload the project database.",
                "If the unit does not respond to Toolkit, remove 240V and C-Bus for 5 minutes to force a full reset.",
                "If the unit remains unresponsive after reset, the internal microcontroller or EEPROM has failed. Replace the dimmer.",
                "Always complete a Toolkit 'Verify' after uploading to confirm all group addresses are correctly programmed."
            ]
        }
    },
    "5000CT": {
        "blinking-led-codes": {
            "answer": "The 5000CT black and white touch screen blinking indicates a boot failure. A blinking cursor after the splash screen means the CompactFlash card or RAM module has failed. The unit half-boots but never reaches the main menu. Pushing the reset button behind the glass temporarily restores function, but the fault returns within hours as the failing component warms up and fails.",
            "steps": [
                "Remove power and reseat the CF card (behind the rear cover). If the screen boots, the CF card was dislodged.",
                "Replace the CF card with an industrial-grade card <2GB FAT16 formatted. Use a known-good CF with the correct firmware image from PICED.",
                "If the blinking persists, the RAM module (72-pin SO-DIMM between the two PCBs on CTC1/CTC3 units) has failed. Replace the RAM module.",
                "For the 5000CT2 (black and white), the electroluminescent backlight inverter may also fail — listen for the 400Hz inverter whine. If absent, the inverter module needs replacement."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "A 5000CT that powers on (backlight glows) but the screen is frozen with no touch response typically has a failed touch overlay. The resistive touch overlay degrades after 6-8 years of use. The C-Bus side of the screen still functions (it continues to respond to C-Bus commands and update its display), but the touch layer no longer registers presses.",
            "steps": [
                "Check if the screen display updates when C-Bus commands are sent (e.g. dimmer levels change). If the display updates, the C-Bus transceiver is working.",
                "If touch is unresponsive but the display works, the touch overlay or its ribbon cable has failed. JEA Technologies in Nunawading VIC replaces touch overlays for approximately $300-$500 AUD.",
                "Replacement option: upgrade to a 5080CTC3 colour touch screen (current Clipsal model).",
                "Alternative: replace the 5000CT with a HomeGate software installation on an iPad running in kiosk mode."
            ]
        }
    },
    "5080CTC": {
        "blinking-led-codes": {
            "answer": "The 5080CTC colour touch screen blinking or dimming indicates a failing internal PSU. The backlight inverter board produces a characteristic whine at approximately 400Hz when working correctly. If the screen brightness fluctuates or the display is dim, the CCFL backlight tube or inverter module is failing. The CTC1 and CTC2 revisions are more prone to this than the CTC3.",
            "steps": [
                "Listen for the 400Hz inverter whine near the top edge of the screen. If absent or intermittent, the inverter module needs replacement.",
                "Check the screen brightness in Settings > Display. If full brightness is selected but the screen is dim, the CCFL tube has reached end of life.",
                "Arbor Australia (the original manufacturer) still repairs all three revisions of the 5080CTC. Contact them for RMA.",
                "The CTC3 revision has an improved backlight driver circuit with extended life. Upgrade if replacing a CTC1 or CTC2."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "A 5080CTC that displays C-Bus status (updates level indicators) but does not transmit commands when buttons are pressed has a 'transmit error'. This is a known failure of the transmit circuit on the main PCB. Measuring the C-Bus voltage drop across the CTC confirms the fault: if voltage drops by more than 1.5V when the CTC is connected, the transmit IC has a low-impedance fault.",
            "steps": [
                "Measure C-Bus voltage at the CTC's RJ45 with the unit connected and disconnected. A drop >1.5V when connected confirms transmit circuit failure.",
                "Check firmware version: Settings > Information. If below 4.13.1.45, update via PICED. Some transmit errors are fixed in newer firmware.",
                "If the voltage drop test confirms hardware failure, the CTC must be removed for repair by Arbor Australia or JEA Technologies.",
                "As a temporary workaround, disconnect the CTC from C-Bus. The loss of voltage drop may restore network stability for other devices."
            ]
        }
    },
    "5200WHC2": {
        "blinking-led-codes": {
            "answer": "The 5200WHC2 Wiser 2 C-Bus LED blinking red after a factory reset indicates a project configuration mismatch. The most common cause is the control system type being set to 'C-Bus Home Controller' instead of 'Wiser 2' in PICED. The Wiser 2 and the newer SpaceLogic Home Controller (SLHC) share the exact same 5200WHC2 part number but require completely different firmware images — flashing the wrong one bricks the C-Bus interface until another factory reset.",
            "steps": [
                "In PICED, open Options > Project Settings > Control System Type. Set to 'Wiser 2' (not 'C-Bus Home Controller' or 'SLHC').",
                "Perform a full factory reset: hold the reset button behind the access hole for 10 seconds using a paperclip.",
                "After reset, create a new blank project in PICED with the correct control system type and upload to the Wiser 2.",
                "If the C-Bus LED stays red with a known-good project, the internal C-Bus transceiver (Silicon Labs CP210x) may be damaged.",
                "For SLHC firmware, download the latest from the Schneider Electric portal. Wiser 2 firmware and SLHC firmware are NOT interchangeable."
            ]
        },
        "frozen-unresponsive-interfaces": {
            "answer": "A 5200WHC2 that is powered but unresponsive to PICED or the web interface has experienced a firmware crash. The Wiser 2 runs Linux on an ARM processor and the root filesystem can become corrupted from unsafe power-downs. The device may still respond to ICMP ping but refuse all management connections.",
            "steps": [
                "Attempt to ping the Wiser 2's IP address. If it responds, try to SSH to the device using the default credentials.",
                "If SSH fails, perform a hardware factory reset using the rear reset button (hold 10 seconds until all LEDs flash).",
                "After reset, reconnect via PICED using USB (the mini-USB port on the front panel).",
                "Reload the project from a known-good backup file. Do NOT use a stale backup from before the corruption.",
                "If none of the above works, the internal SD card or eMMC flash has failed. The 5200WHC2 needs replacement."
            ]
        }
    },
    "L5508D2A": {},
    "L5504D2U": {}
}

# Map issue types to default answer patterns
ISSUE_CONTENT = {
    "blinking-led-codes": {
        "other": {
            "answer": "Blinking LED codes on this device indicate a communication fault or hardware error. The exact blink pattern determines the specific failure mode. Refer to the manufacturer's documentation for blink pattern decoding, or contact our diagnostic service for toolkit analysis.",
            "steps": []
        }
    },
    "buzzing-or-clicking-noises": {
        "other": {
            "answer": "Audible buzzing or clicking from lighting control equipment indicates either a failing internal power supply or a relay/dimmer component operating outside its design parameters. Do not ignore these sounds — they often precede complete hardware failure.",
            "steps": []
        }
    },
    "frozen-unresponsive-interfaces": {
        "other": {
            "answer": "A frozen or unresponsive controller typically results from a microcontroller lockup caused by electrical noise, brownout, or corrupted firmware. A full power cycle (remove all power for 2 minutes) resolves approximately 60% of these cases.",
            "steps": []
        }
    },
    "lost-schedules-and-clock-drift": {
        "other": {
            "answer": "Lost schedules and clock drift are almost always caused by a failed CR2032 coin cell battery on the network's designated Clock Driver device. The battery has a typical lifespan of 5-7 years. When it fails, the real-time clock resets to 1-Jan-2000 on every power cycle.",
            "steps": []
        }
    },
    "stuck-on-channels": {
        "other": {
            "answer": "Channels stuck on full brightness or fully off indicate a failed output component — either a welded relay contact or a shorted triac/diming MOSFET. This is a hardware fault that requires component-level replacement of the affected output device.",
            "steps": []
        }
    },
    "surge-storm-damage": {
        "other": {
            "answer": "Electrical surge damage from lightning or grid switching events typically destroys the internal power supply and communication transceivers. Multiple devices failing simultaneously on the same network strongly indicates a mains-borne surge event.",
            "steps": []
        }
    }
}

# Inject unique content
count = 0
for f in glob.glob('tech-library/*.html'):
    try:
        with open(f, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
    except:
        continue

    # Extract model and issue from filename
    name = f.replace('tech-library\\', '').replace('.html', '')
    # Patterns: brand-model-issue-region or brand-model-issue
    # Eg. clipsal-c-bus-5500pc-blinking-led-codes-eastern-suburbs
    #     dynalite-ddbc1200-blinking-led-codes-eastern-suburbs

    parts = name.split('-')
    model = None
    issue_type = None
    brand = 'Clipsal C-Bus' if 'clipsal' in name else 'Dynalite'

    # Known models to match
    known_models = ['5500pc', '5500cn', 'l5508d1a', 'l5508d2a', 'l5512rvf', '5508rvf',
                    '5504amp', '5502dal', 'l5504d2u', '5000ct', '5080ctc', '5200whc2',
                    'ddbc1200', 'ddmc802', 'ddng232', 'ddng485', 'ddrc1210', 'ddrc1220',
                    'dmdr12-320', 'dus360cs', 'antumbra', 'pdeg']

    fname_lower = name.lower().replace('clipsal-c-bus-', '').replace('dynalite-', '')
    
    # Find which model this is
    for km in known_models:
        if km in fname_lower:
            model = km
            break
    
    # Find issue type
    known_issues = ['blinking-led-codes', 'buzzing-or-clicking-noises', 
                    'frozen-unresponsive-interfaces', 'lost-schedules-and-clock-drift',
                    'stuck-on-channels', 'surge-storm-damage']
    
    for ki in known_issues:
        if ki in fname_lower:
            issue_type = ki
            break

    if not model or not issue_type:
        continue

    # Get content for this model + issue
    device_content = CONTENT.get(model.upper(), {})
    issue_data = device_content.get(issue_type, None)

    if not issue_data:
        # Fall back to generic issue content
        issue_data = ISSUE_CONTENT.get(issue_type, {}).get('other', None)
        if not issue_data:
            continue

    # Build the new unique content block
    steps_html = ''
    for step in issue_data['steps']:
        steps_html += f'<li>{step}</li>'

    answer_html = issue_data['answer']

    new_direct_answer = f'''<p style="font-size:18px; line-height:1.6;"><strong>{answer_html}</strong></p>
                        
                        <h3 style="margin-top:40px;">Step-by-Step Diagnostic Steps</h3>
                        <ol style="margin-left:20px; line-height:1.8; font-size:16px;">
                            {steps_html}
                        </ol>'''

    # Replace the existing Direct Answer section
    old_pattern = r'<h2>Direct Answer:.*?</h2>\s*<p style="font-size:18px; line-height:1\.6;"><strong>.*?</strong></p>\s*<h3 style="margin-top:40px;">Step-by-Step Diagnostic Steps</h3>\s*<ol style="margin-left:20px; line-height:1\.8; font-size:16px;">.*?</ol>'
    
    old_direct = re.search(old_pattern, content, re.DOTALL)
    if not old_direct:
        continue

    old_text = old_direct.group(0)

    # Replace the content between <h2> and after </ol>
    # The h2 heading with device name stays, but the rest gets replaced
    h2_match = re.search(r'<h2>Direct Answer:.*?</h2>', old_text)
    if not h2_match:
        continue
    
    new_section = h2_match.group(0) + '\n    ' + new_direct_answer
    
    content = content.replace(old_text, new_section)
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    
    count += 1
    if count % 50 == 0:
        print(f'Processed {count} files...')

print(f'\nTotal tech-library files updated: {count}')
