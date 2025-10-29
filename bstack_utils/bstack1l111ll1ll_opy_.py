# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack111l1ll1_opy_
from bstack_utils.helper import bstack1l11l111_opy_
logger = logging.getLogger(__name__)
def bstack111l1ll1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1111l1111_opy_(context, *args):
    tags = getattr(args[0], bstack11l11ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ᭶"), [])
    bstack11lll1lll_opy_ = bstack111l1ll1_opy_.bstack111l1lll1_opy_(tags)
    threading.current_thread().isA11yTest = bstack11lll1lll_opy_
    try:
      bstack1l1111l1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1ll1l_opy_(bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ᭷")) else context.browser
      if bstack1l1111l1ll_opy_ and bstack1l1111l1ll_opy_.session_id and bstack11lll1lll_opy_ and bstack1l11l111_opy_(
              threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᭸"), None):
          threading.current_thread().isA11yTest = bstack111l1ll1_opy_.bstack1ll1l1l111_opy_(bstack1l1111l1ll_opy_, bstack11lll1lll_opy_)
    except Exception as e:
       logger.debug(bstack11l11ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬ᭹").format(str(e)))
def bstack111llll11l_opy_(bstack1l1111l1ll_opy_):
    if bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ᭺"), None) and bstack1l11l111_opy_(
      threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭻"), None) and not bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࠫ᭼"), False):
      threading.current_thread().a11y_stop = True
      bstack111l1ll1_opy_.bstack1111llll_opy_(bstack1l1111l1ll_opy_, name=bstack11l11ll_opy_ (u"ࠤࠥ᭽"), path=bstack11l11ll_opy_ (u"ࠥࠦ᭾"))