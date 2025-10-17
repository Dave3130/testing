# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from bstack_utils.helper import bstack1l1lllll_opy_
logger = logging.getLogger(__name__)
def bstack111l111l11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack111l1l1l1l_opy_(context, *args):
    tags = getattr(args[0], bstack11111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᬩ"), [])
    bstack11ll111lll_opy_ = bstack1lll1ll1l_opy_.bstack11l1lllll_opy_(tags)
    threading.current_thread().isA11yTest = bstack11ll111lll_opy_
    try:
      bstack1111l1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack111l111l11_opy_(bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩᬪ")) else context.browser
      if bstack1111l1111l_opy_ and bstack1111l1111l_opy_.session_id and bstack11ll111lll_opy_ and bstack1l1lllll_opy_(
              threading.current_thread(), bstack11111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᬫ"), None):
          threading.current_thread().isA11yTest = bstack1lll1ll1l_opy_.bstack1lll1111l1_opy_(bstack1111l1111l_opy_, bstack11ll111lll_opy_)
    except Exception as e:
       logger.debug(bstack11111_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬᬬ").format(str(e)))
def bstack1ll1l1l1ll_opy_(bstack1111l1111l_opy_):
    if bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪᬭ"), None) and bstack1l1lllll_opy_(
      threading.current_thread(), bstack11111_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᬮ"), None) and not bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࠫᬯ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll1ll1l_opy_.bstack1llll1l1l_opy_(bstack1111l1111l_opy_, name=bstack11111_opy_ (u"ࠤࠥᬰ"), path=bstack11111_opy_ (u"ࠥࠦᬱ"))