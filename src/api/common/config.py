from environs import Env

env = Env()

config = {
    'DB_HOST': env.str('DB_HOST', 'localhost'),
    'DB_PORT': env.int('DB_PORT', '8086')
}
