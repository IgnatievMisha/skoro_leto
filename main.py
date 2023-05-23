import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename="logs.log", filemode="w")
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")
try:
    print(10/0)
except(Exception):
    logging.exception(":(")




#factorial
def factorial(n):
    logging.info(f"start calculating factorial {n}")
    result = 1
    for i in range(1, n+1):
        result*=i
    logging.info("finish")
    print(result)

factorial(5)