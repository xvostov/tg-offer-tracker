from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAddCategoryAvito1(StatesGroup):
    get_url = State()


class FSMRemoveCategoryAvito1(StatesGroup):
    get_url = State()


class FSMAddCategoryAvito2(StatesGroup):
    get_url = State()


class FSMRemoveCategoryAvito2(StatesGroup):
    get_url = State()


class FSMAddToBlackList(StatesGroup):
    get_id = State()


class FSMRemoveFromBlackList(StatesGroup):
    get_id = State()


class FSMAddStopWord(StatesGroup):
    word = State()


class FSMRemoveStopWord(StatesGroup):
    word = State()


class FSMAddUser(StatesGroup):
    get_chat_id = State()


class FSMRemoveUser(StatesGroup):
    get_chat_id = State()


class FSMAddCategoryOlx1(StatesGroup):
    get_url = State()


class FSMRemoveCategoryOlx1(StatesGroup):
    get_url = State()


class FSMAddCategoryWatch(StatesGroup):
    get_url = State()


class FSMRemoveCategoryWatch(StatesGroup):
    get_url = State()


class FSMAddToBlackListOlx(StatesGroup):
    get_id = State()


class FSMRemoveFromBlackListOlx(StatesGroup):
    get_id = State()


class FSMAddStopwordOlx(StatesGroup):
    word = State()


class FSMRemoveStopwordOlx(StatesGroup):
    word = State()


class FSMAddCategoryLalafo(StatesGroup):
    get_url = State()


class FSMRemoveCategoryLalafo(StatesGroup):
    get_url = State()


class FSMAddStopWordLalafo(StatesGroup):
    word = State()


class FSMRemoveStopWordLalafo(StatesGroup):
    word = State()


class FSMAddCategoryYoula(StatesGroup):
    get_url = State()


class FSMRemoveCategoryYoula(StatesGroup):
    get_url = State()


class FSMAddCategoryAvito3(StatesGroup):
    get_url = State()


class FSMRemoveCategoryAvito3(StatesGroup):
    get_url = State()


class FSMAddCategoryWatch2(StatesGroup):
    get_url = State()


class FSMRemoveCategoryWatch2(StatesGroup):
    get_url = State()



class FSMAddMinPrice(StatesGroup):
    get_url = State()
    get_min_price = State()

class FSMRemoveMinPrice(StatesGroup):
    get_url = State()
