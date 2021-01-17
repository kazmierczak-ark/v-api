from environs import Env

env = Env()

config = {
    'DB_HOST': env.str('DB_HOST', 'localhost'),
    'DB_PORT': env.int('DB_PORT', '8086'),
    'CALCULATE_API_HOST': env.str('CALCULATE_API_HOST', 'localhost'),
    'CALCULATE_API_PORT': env.int('CALCULATE_API_PORT', '5000')
}
