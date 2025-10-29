# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lllll1l1_opy_
from bstack_utils.helper import bstack1lllll11_opy_
logger = logging.getLogger(__name__)
def bstack1ll1l11lll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1lll11llll_opy_(context, *args):
    tags = getattr(args[0], bstack11ll1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ᭶"), [])
    bstack1ll1ll111_opy_ = bstack1lllll1l1_opy_.bstack111l1ll11_opy_(tags)
    threading.current_thread().isA11yTest = bstack1ll1ll111_opy_
    try:
      bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l11lll_opy_(bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ᭷")) else context.browser
      if bstack111l1lll1_opy_ and bstack111l1lll1_opy_.session_id and bstack1ll1ll111_opy_ and bstack1lllll11_opy_(
              threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᭸"), None):
          threading.current_thread().isA11yTest = bstack1lllll1l1_opy_.bstack1l11llll1l_opy_(bstack111l1lll1_opy_, bstack1ll1ll111_opy_)
    except Exception as e:
       logger.debug(bstack11ll1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡢ࠳࠴ࡽࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬ᭹").format(str(e)))
def bstack1ll11lllll_opy_(bstack111l1lll1_opy_):
    if bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ᭺"), None) and bstack1lllll11_opy_(
      threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭻"), None) and not bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡥࡳࡵࡱࡳࠫ᭼"), False):
      threading.current_thread().a11y_stop = True
      bstack1lllll1l1_opy_.bstack1lll111ll_opy_(bstack111l1lll1_opy_, name=bstack11ll1l_opy_ (u"ࠤࠥ᭽"), path=bstack11ll1l_opy_ (u"ࠥࠦ᭾"))