def hisob_funksiya(son: float) -> dict:
    """
    Alohida ajratilgan Serverless / Microservice hisob-kitob funksiyasi.
    Monolit ilovadan mustaqil mantiqni alohida blokda bajaradi.
    """
    return {
        "rejim": "Serverless / Microservice (ajratilgan funksiya)",
        "son": son,
        "kvadrat": son ** 2,
        "ikki_barobar": son * 2,
        "xabar": "Funksiya muvaffaqiyatli bajarildi"
    }