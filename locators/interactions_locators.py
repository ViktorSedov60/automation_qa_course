from selenium.webdriver.common.by import By


class SortableLocator:
    TAB_LIST = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'div#demo-tabpane-list div.list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div#demo-tabpane-grid div.list-group-item')


class SelectableLocator:
    LIST_TAB = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'ul#verticalListContainer li')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'ul#verticalListContainer li.active')

    GRID_TAB = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div#gridContainer li')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'div#gridContainer li.active')

class ResizableLocator:
    RESIZABLE_BOX = (By.ID, 'resizableBoxWithRestriction')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div#resizableBoxWithRestriction span.react-resizable-handle')

    RESIZABLE = (By.ID, 'resizable')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')

class DroppableLocator:
    SIMPLE = (By.CSS_SELECTOR, 'a#droppableExample-tab-simple')
    DRAG_ME = (By.CSS_SELECTOR, 'div#draggable')
    DROP_HERE = (By.CSS_SELECTOR, 'div#simpleDropContainer div#droppable')


    ACCEPT = (By.CSS_SELECTOR, 'a#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div#acceptable')
    NOT_ACCEPTABLE = (By.ID, 'notAcceptable')
    DROP_HERE_ACCERT = (By.CSS_SELECTOR, 'div#acceptDropContainer div#droppable')
    DROP_HERE_ACCERT_AFTER = (By.CSS_SELECTOR, 'div#acceptDropContainer div#droppable.ui-state-highlight')

    PREVENT_PROPOGATION = (By.CSS_SELECTOR, 'a#droppableExample-tab-preventPropogation')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, 'div#dragBox')
    OUTER_DROPPABLE = (By.CSS_SELECTOR, 'div#notGreedyDropBox p')
    INNER_DROPPABLE = (By.CSS_SELECTOR, 'div#notGreedyInnerDropBox p')
    OUTER_DROPPABLE_GREEDY = (By.CSS_SELECTOR, 'div#greedyDropBox p')
    INNER_DROPPABLE_GREEDY = (By.CSS_SELECTOR, 'div#greedyDropBoxInner p')


    REVERT_DRAGGABLE = (By.CSS_SELECTOR, 'a#droppableExample-tab-revertable')
    WILL_REVERT = (By.CSS_SELECTOR, 'div#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, 'div#notRevertable')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, 'div#revertableDropContainer div#droppable')


class DragabbleLocator:
    SIMPLE = (By.ID, 'draggableExample-tab-simple')
    DRAG_MY = (By.ID, 'dragBox')

    AXIS_RESTRICTED = (By.ID, 'draggableExample-tab-axisRestriction')
    ONLI_X = (By.ID, 'restrictedX')
    ONLI_Y = (By.ID, 'restrictedY')

    CONTAINER_RESTRICTED = (By.ID, 'draggableExample-tab-containerRestriction')
    THE_BOX = (By.CSS_SELECTOR, 'div.draggable.ui-widget-content.ui-draggable')
    MY_PARENT = (By.CSS_SELECTOR, 'span.ui-widget-header.ui-draggable')

    CURSOR_STYLE = (By.ID, 'draggableExample-tab-cursorStyle')
    CENTER_CURSOR = (By.ID, 'cursorCenter')
    TOP_LEFT_CURSOR = (By.ID, 'cursorTopLeft')
    BOTTOM_CURSOR = (By.ID, 'cursorBottom')

