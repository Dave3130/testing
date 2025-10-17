# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack11l111l1_opy_
from bstack_utils.helper import bstack1l11lll1_opy_
logger = logging.getLogger(__name__)
def bstack111l1ll1ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1111111l1_opy_(context, *args):
    tags = getattr(args[0], bstack11l111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᬩ"), [])
    bstack1ll1l1l11l_opy_ = bstack11l111l1_opy_.bstack1l11111ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack1ll1l1l11l_opy_
    try:
      bstack11l1ll11ll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1ll1ll_opy_(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩᬪ")) else context.browser
      if bstack11l1ll11ll_opy_ and bstack11l1ll11ll_opy_.session_id and bstack1ll1l1l11l_opy_ and bstack1l11lll1_opy_(
              threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᬫ"), None):
          threading.current_thread().isA11yTest = bstack11l111l1_opy_.bstack111l11lll1_opy_(bstack11l1ll11ll_opy_, bstack1ll1l1l11l_opy_)
    except Exception as e:
       logger.debug(bstack11l111_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬᬬ").format(str(e)))
def bstack11l1111l1_opy_(bstack11l1ll11ll_opy_):
    if bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪᬭ"), None) and bstack1l11lll1_opy_(
      threading.current_thread(), bstack11l111_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᬮ"), None) and not bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࠫᬯ"), False):
      threading.current_thread().a11y_stop = True
      bstack11l111l1_opy_.bstack11l11lll_opy_(bstack11l1ll11ll_opy_, name=bstack11l111_opy_ (u"ࠤࠥᬰ"), path=bstack11l111_opy_ (u"ࠥࠦᬱ"))