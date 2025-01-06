import logging

logger = logging.getLogger('name')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')


debug_handler = logging.FileHandler(filename='debug_info.log', mode='a', encoding='UTF-8')
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

warnings_handler = logging.FileHandler(filename='warnings_errors.log', mode='a', encoding='UTF-8')
warnings_handler.setLevel(logging.WARNING)
warnings_handler.setFormatter(formatter)


logger.addHandler(debug_handler)
logger.addHandler(warnings_handler)


logger.debug('Работать, негры, солнце еще высоко(с)...')
logger.info('Просто информация, просто ни о чем.')
logger.warning('Горячо, очень горячо!')
logger.error('Эррор! Эррор!')
logger.critical('Ну все, допрыгались!')

