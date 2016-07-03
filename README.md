# Toja Travels Tokyo like Native (Ninja).
This application's goal is to make Traveling to Tokyo effortless and fun. Our target will be tourists (Homo sapiens) who want to make the most of their first experience in Japan. 

Our app will provide a protocol for tourists to explore their options, make reservations and go to places without using a single word of Japanese.

For the prototype, our frontend is built with Angular JS (Material Design), while the backend is built with django.

Our system use two second generation ECS instances on Alicloud, a MySQL DB on ApsaraDB and use SLB to direct Internet to ECS.

# Toja Backend
In `server/`: 

    python manage.py 0.0.0.0

# Toja Client

## Build & development

Run `grunt` for building and `grunt serve` for preview.

## Contributors

* Tonny Pham (jwall149@gmail.com)
* Thinh Pham (nhim175@gmail.com)
* Conrad de Kerckhove (conrad.dekerckhove@gmail.com)
* Phong Nguyen (xphongvn@gmail.com)

## License

MIT
