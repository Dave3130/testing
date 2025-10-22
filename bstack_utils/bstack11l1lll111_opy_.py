# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lll11ll1_opy_
from bstack_utils.helper import bstack1l11l1ll_opy_
logger = logging.getLogger(__name__)
def bstack1l1l11ll11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1ll1l1lll_opy_(context, *args):
    tags = getattr(args[0], bstack111l1l_opy_ (u"࠭ࡴࡢࡩࡶࠫ᭗"), [])
    bstack1111lllll1_opy_ = bstack1lll11ll1_opy_.bstack1l1ll11lll_opy_(tags)
    threading.current_thread().isA11yTest = bstack1111lllll1_opy_
    try:
      bstack111ll11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11ll11_opy_(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭᭘")) else context.browser
      if bstack111ll11111_opy_ and bstack111ll11111_opy_.session_id and bstack1111lllll1_opy_ and bstack1l11l1ll_opy_(
              threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ᭙"), None):
          threading.current_thread().isA11yTest = bstack1lll11ll1_opy_.bstack1lll1lll11_opy_(bstack111ll11111_opy_, bstack1111lllll1_opy_)
    except Exception as e:
       logger.debug(bstack111l1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡦ࠷࠱ࡺࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ᭚").format(str(e)))
def bstack1l1111lll1_opy_(bstack111ll11111_opy_):
    if bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ᭛"), None) and bstack1l11l1ll_opy_(
      threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᭜"), None) and not bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࠨ᭝"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll11ll1_opy_.bstack111l11ll_opy_(bstack111ll11111_opy_, name=bstack111l1l_opy_ (u"ࠨࠢ᭞"), path=bstack111l1l_opy_ (u"ࠢࠣ᭟"))