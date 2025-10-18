# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1111ll11_opy_
from bstack_utils.helper import bstack1l1l11l1_opy_
logger = logging.getLogger(__name__)
def bstack1lll1111l1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1l111l1ll_opy_(context, *args):
    tags = getattr(args[0], bstack11ll_opy_ (u"࠭ࡴࡢࡩࡶࠫ᭞"), [])
    bstack1ll1l11lll_opy_ = bstack1111ll11_opy_.bstack11l11lll1_opy_(tags)
    threading.current_thread().isA11yTest = bstack1ll1l11lll_opy_
    try:
      bstack1l1ll1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll1111l1_opy_(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭᭟")) else context.browser
      if bstack1l1ll1l11l_opy_ and bstack1l1ll1l11l_opy_.session_id and bstack1ll1l11lll_opy_ and bstack1l1l11l1_opy_(
              threading.current_thread(), bstack11ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ᭠"), None):
          threading.current_thread().isA11yTest = bstack1111ll11_opy_.bstack1ll11lll1_opy_(bstack1l1ll1l11l_opy_, bstack1ll1l11lll_opy_)
    except Exception as e:
       logger.debug(bstack11ll_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡦ࠷࠱ࡺࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ᭡").format(str(e)))
def bstack1l11l11ll_opy_(bstack1l1ll1l11l_opy_):
    if bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ᭢"), None) and bstack1l1l11l1_opy_(
      threading.current_thread(), bstack11ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᭣"), None) and not bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࠨ᭤"), False):
      threading.current_thread().a11y_stop = True
      bstack1111ll11_opy_.bstack111ll1l1_opy_(bstack1l1ll1l11l_opy_, name=bstack11ll_opy_ (u"ࠨࠢ᭥"), path=bstack11ll_opy_ (u"ࠢࠣ᭦"))