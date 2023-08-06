from Home import WebApp

web_content = """
            Hi, I am MAM! I am a Python programmer, teacher, and founder of TechLumos. I graduated in 2023 with a Bachelors of Electrical Engineering in Power/Microwave/Embedded/Communication from NUST H-12, Islamabad with a focus on using Python for nothing.
            """
web_app = WebApp(image="images/photo.jpeg",
                 name="M | Aasif | M",
                 content=web_content)

web_app._build_web_app_()
