# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack111ll1ll_opy_
from bstack_utils.helper import bstack1ll111ll_opy_
logger = logging.getLogger(__name__)
def bstack1l11111l1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1l1111ll1l_opy_(context, *args):
    tags = getattr(args[0], bstack1lll11l_opy_ (u"ࠬࡺࡡࡨࡵࠪ᭫"), [])
    bstack11lll1lll1_opy_ = bstack111ll1ll_opy_.bstack111111l1l1_opy_(tags)
    threading.current_thread().isA11yTest = bstack11lll1lll1_opy_
    try:
      bstack1111l11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11111l1l_opy_(bstack1lll11l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶ᭬ࠬ")) else context.browser
      if bstack1111l11111_opy_ and bstack1111l11111_opy_.session_id and bstack11lll1lll1_opy_ and bstack1ll111ll_opy_(
              threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭭"), None):
          threading.current_thread().isA11yTest = bstack111ll1ll_opy_.bstack1111l11l1l_opy_(bstack1111l11111_opy_, bstack11lll1lll1_opy_)
    except Exception as e:
       logger.debug(bstack1lll11l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨ᭮").format(str(e)))
def bstack11ll1ll1l1_opy_(bstack1111l11111_opy_):
    if bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭᭯"), None) and bstack1ll111ll_opy_(
      threading.current_thread(), bstack1lll11l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᭰"), None) and not bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧ᭱"), False):
      threading.current_thread().a11y_stop = True
      bstack111ll1ll_opy_.bstack111lll11_opy_(bstack1111l11111_opy_, name=bstack1lll11l_opy_ (u"ࠧࠨ᭲"), path=bstack1lll11l_opy_ (u"ࠨࠢ᭳"))