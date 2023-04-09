import json
from solution import parse_address


if __name__ == "__main__":
    addresses = [
        "Winterallee 3",
        "Musterstrasse 45",
        "Blaufeldweg 123B",
        "Am Bächle 23",
        "Auf der Vogelwiese 23 b",
        "4, rue de la revolution",
        "200 Broadway Av",
        "Calle Aduana, 29",
        "Calle 39 No 1540",
        "ul. Korfantego 2",
        "P.O. Box 1234",
        "1000 S 4th St, Apt 1",
        "Igloo 42",
        "Piazza San Marco 5",
        "12 bis, avenue Foch",
        "2000 Pennsylvania Ave NW",
        "Storgatan 1 Lgh 1001",
        "21, rue St-Germain-des-Prés",
        "30 West Twenty-sixth St",
        "5th Avenue 200",
        "1st Avenue 200",
        "E 45th St 200",
        "N 5th St 200",
        "Potsdamer Straße 58, Haus 23",
        "rue de la république, 154",
        "11, Jalan Kuchai Maju 7/116b",
        "Königstraße 10",
        "Friedrich-Wilhelm-Straße 3",
        "Winterallee 3b",
        "Musterstraße 5c",
        "Via della Lungara, 231/233",
        "Calle 20, No. 32F-52",
        "21 BIS RUE DU SIMPLON",
        "Via S. Antonio 4/b",
        "100, rue de la gare",
        "3-4-5 Roppongi",
        "",
        "   ",
        "123",
        "No address",
        "12345 67890"
    ]

    for addr in addresses:
        try:
            result = parse_address(addr)
            print(f"{addr} -> {json.dumps(result)}")
        except ValueError as e:
            print(f"{addr} -> {str(e)}")