import sympy as sp

from module.util.logger_conf import logger


def find_limit() -> None:
    x: sp.Symbol = sp.symbols("x");
    logger.info(f"x = {x}")
    lim = sp.limit(sp.sin(x), x, 0, dir="-")
    logger.info(f"lim:{lim}")
    return


def find_derivate() -> None:
    return

def find_integrate() -> None:
    x = sp.symbols('x')
    expr = x**2 + x + 1 
    integrate = sp.integrate(expr, x)
    # sp.init_session()
    logger.info(f"integrate:{integrate}")
    logger.info(f"integrate eval:{integrate.subs({x:3})}")
    # sp.pprint(expr=expr)
    return

if __name__ == "__main__":
    # sp.init_printing()
    find_integrate()
    pass