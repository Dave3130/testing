# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack11111111_opy_
from bstack_utils.helper import bstack1l1111ll_opy_
logger = logging.getLogger(__name__)
def bstack1ll1l11ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11l11l1l11_opy_(context, *args):
    tags = getattr(args[0], bstack1l111ll_opy_ (u"࠭ࡴࡢࡩࡶࠫ᭗"), [])
    bstack11111lll1_opy_ = bstack11111111_opy_.bstack1ll1ll1ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack11111lll1_opy_
    try:
      bstack1l1lll11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l11ll_opy_(bstack1l111ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭᭘")) else context.browser
      if bstack1l1lll11l_opy_ and bstack1l1lll11l_opy_.session_id and bstack11111lll1_opy_ and bstack1l1111ll_opy_(
              threading.current_thread(), bstack1l111ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ᭙"), None):
          threading.current_thread().isA11yTest = bstack11111111_opy_.bstack1l1ll1ll1l_opy_(bstack1l1lll11l_opy_, bstack11111lll1_opy_)
    except Exception as e:
       logger.debug(bstack1l111ll_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡦ࠷࠱ࡺࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ᭚").format(str(e)))
def bstack11l1l11lll_opy_(bstack1l1lll11l_opy_):
    if bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ᭛"), None) and bstack1l1111ll_opy_(
      threading.current_thread(), bstack1l111ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᭜"), None) and not bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࠨ᭝"), False):
      threading.current_thread().a11y_stop = True
      bstack11111111_opy_.bstack1111111l_opy_(bstack1l1lll11l_opy_, name=bstack1l111ll_opy_ (u"ࠨࠢ᭞"), path=bstack1l111ll_opy_ (u"ࠢࠣ᭟"))