
import requests


def check_security_headers(url):
    """Check security headers on a website."""

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        headers = response.headers

        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        print("\n==============================")
        print("      CYBERRECON")
        print(" Website Security Header Check")
        print("==============================")

        print(f"\nTarget: {response.url}")
        print(f"Status Code: {response.status_code}")

        print("\nSecurity Headers:\n")

        for header in security_headers:
            if header in headers:
                print(f"[FOUND] {header}")
            else:
                print(f"[MISSING] {header}")

    except requests.RequestException as error:
        print(f"Connection error: {error}")


def main():
    url = input("Enter website URL: ")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    check_security_headers(url)


if __name__ == "__main__":
    main()