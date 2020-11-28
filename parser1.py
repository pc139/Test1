import argparse

def parse_arguments (city, country):
    parser=argparse.ArgumentParser(
         description="Weather Forecast for the next 16 days",

    parser.add_argument("-v", help= "be more verbose", action="store_true")

    parser.add_argument ("city",
                         type=str,
                         help= "allowed cities: 'Catania', 'Bari', 'Firenze', 'Bologna',
                              'Genova', 'Palermo', 'Torino', 'Milano', 'Roma',
                        choices = ["Catania", "Bari", "Firenze", "Bologna", "Genova",
                                   "Palermo", "Torino", "Milano", "Roma"])

    parser.add_argument("country",
                        type=str,
                        help="Input consentiti: Italy",
                         choices = ["Italy"])

    args = parser.parse_args()
    return args
