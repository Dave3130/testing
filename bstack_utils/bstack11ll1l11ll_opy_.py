# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack11111ll1_opy_
from bstack_utils.helper import bstack1l1lll11_opy_
logger = logging.getLogger(__name__)
def bstack11111l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11l1111ll1_opy_(context, *args):
    tags = getattr(args[0], bstack1ll1ll1_opy_ (u"ࠧࡵࡣࡪࡷࠬᬼ"), [])
    bstack111ll1llll_opy_ = bstack11111ll1_opy_.bstack111llllll_opy_(tags)
    threading.current_thread().isA11yTest = bstack111ll1llll_opy_
    try:
      bstack111ll1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack11111l11l_opy_(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧᬽ")) else context.browser
      if bstack111ll1ll1_opy_ and bstack111ll1ll1_opy_.session_id and bstack111ll1llll_opy_ and bstack1l1lll11_opy_(
              threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᬾ"), None):
          threading.current_thread().isA11yTest = bstack11111ll1_opy_.bstack111ll1ll1l_opy_(bstack111ll1ll1_opy_, bstack111ll1llll_opy_)
    except Exception as e:
       logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡧ࠱࠲ࡻࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪᬿ").format(str(e)))
def bstack1l1l1l11l_opy_(bstack111ll1ll1_opy_):
    if bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨᭀ"), None) and bstack1l1lll11_opy_(
      threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᭁ"), None) and not bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࠩᭂ"), False):
      threading.current_thread().a11y_stop = True
      bstack11111ll1_opy_.bstack111l111l_opy_(bstack111ll1ll1_opy_, name=bstack1ll1ll1_opy_ (u"ࠢࠣᭃ"), path=bstack1ll1ll1_opy_ (u"ࠣࠤ᭄"))