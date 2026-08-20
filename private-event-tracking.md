# Private event tracking

Sydney Automation Co. now loads `/sac-event-tracking.js` on the homepage, comparison page, C-Bus Repair page, Dynalite Repair page, and C-Bus Upgrade page. The tracker sends events to the existing GA4 property `G-7EZFB6GRJ3` and does not display counts publicly.

## Events

| Event | Trigger | Main dimensions |
|---|---|---|
| `phone_click` | Any `tel:` link | `page_path`, `cta_text`, `destination` |
| `email_click` | Any `mailto:` link | `page_path`, `cta_text`, `destination` |
| `whatsapp_click` | WhatsApp or `wa.me` link | `page_path`, `cta_text`, `destination` |
| `booking_click` | `/book-service` or booking/technician link | `page_path`, `cta_text`, `destination` |
| `quote_click` | `/contact`, quote, enquiry, assessment, or project-details CTA | `page_path`, `cta_text`, `destination` |
| `form_submit` | Any HTML form submission | `page_path`, `form_id`, `form_action` |
| `lead_drawer_open` | Existing lead-capture drawer opened | `source`, `page_location` |
| `lead_path_selected` | Existing lead-capture path selected | `lead_path`, `page_location` |
| `generate_lead` | Existing lead form successfully submitted | `lead_path`, `event_label`, `page_location` |

## GA4 setup

In Google Analytics, open **Admin → Data display → Events**, search for the events above, and mark `phone_click`, `quote_click`, `booking_click`, `form_submit`, and `generate_lead` as key events. For page-by-page reporting, open **Reports → Engagement → Events** or create an Explore report using `Event name` as the row and `Landing page + query string` or `Page path and screen class` as the dimension.

The most useful first comparison is a 28-day report grouped by page path and event name for `/`, `/cbus-repair-sydney`, `/dynalite-repair-sydney`, `/cbus-upgrade-sydney`, and `/cbus-vs-dynalite`.
