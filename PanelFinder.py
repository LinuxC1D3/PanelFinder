import requests

def find_admin_panels(url):
    admin_panels = [
        ("/phpmyadmin", "PHPMyAdmin"),
        ("/wp-admin", "WordPress"),
        (":8447", "Plesk"),
        ("/admin", "Admin"),
        ("/directadmin", "DirectAdmin"),
        (":8080", "ISPConfig"),
        (":10000", "Virtualmin"),
        (":8000", "Ajenti"),
        (":8083", "Vesta Control Panel"),
        ("/froxlor", "Froxlor"),
        (":8090", "CyberPanel"),
        (":2030", "CWP"),
        (":7778", "Kloxo-MR"),
        (":8080", "Sentora"),
        (":8888", "VHCS"),
        (":19999", "Netdata"),
        (":10000", "Webmin")
    ]

    for panel in admin_panels:
        try:
            panel_url = url + panel[0]
            response = requests.get(panel_url)
            if response.status_code == 200:
                print(panel[1], "gefunden:", panel_url)
            else:
                print(panel[1], "nicht gefunden")
        except Exception as e:
            print("Fehler beim Überprüfen von", panel[1], ":", str(e))

# Beispielaufruf des Skripts
if __name__ == "__main__":
    url = input("Bitte geben Sie die URL der Webseite ein: ")
    find_admin_panels(url)