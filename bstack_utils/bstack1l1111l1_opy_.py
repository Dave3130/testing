# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import threading
from bstack_utils.helper import bstack1llll11lll_opy_
from bstack_utils.constants import bstack11l11lll11l_opy_, EVENTS, STAGE
from bstack_utils.bstack11111ll111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1ll_opy_:
    bstack11l11l1l1ll_opy_ = None
    @classmethod
    def bstack11l1l1l1l1_opy_(cls):
        if cls.on() and os.getenv(bstack111111l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧ᫚")):
            logger.info(
                bstack111111l_opy_ (u"ࠨࡘ࡬ࡷ࡮ࡺࠠࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨ᫛").format(os.getenv(bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ᫜"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ᫝"), None) is None or os.environ[bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ᫞")] == bstack111111l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ᫟"):
            return False
        return True
    @classmethod
    def bstack11l11l1ll1l_opy_(cls, bs_config, framework=bstack111111l_opy_ (u"ࠨࠢ᫠")):
        bstack11ll1l11ll1_opy_ = False
        for fw in bstack11l11lll11l_opy_:
            if fw in framework:
                bstack11ll1l11ll1_opy_ = True
        return bstack1llll11lll_opy_(bs_config.get(bstack111111l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ᫡"), bstack11ll1l11ll1_opy_))
    @classmethod
    def bstack11l11l1l111_opy_(cls, framework):
        return framework in bstack11l11lll11l_opy_
    @classmethod
    def bstack11l11l1l1l1_opy_(cls, bs_config, framework):
        return cls.bstack11l11l1ll1l_opy_(bs_config, framework) is True and cls.bstack11l11l1l111_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ᫢"), None)
    @staticmethod
    def bstack1ll1ll1l_opy_():
        if getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᫣"), None):
            return {
                bstack111111l_opy_ (u"ࠪࡸࡾࡶࡥࠨ᫤"): bstack111111l_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ᫥"),
                bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᫦"): getattr(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ᫧"), None)
            }
        if getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ᫨"), None):
            return {
                bstack111111l_opy_ (u"ࠨࡶࡼࡴࡪ࠭᫩"): bstack111111l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ᫪"),
                bstack111111l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᫫"): getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ᫬"), None)
            }
        return None
    @staticmethod
    def bstack11l11l11lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l1ll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1ll1l1_opy_(test, hook_name=None):
        bstack11l11l1l11l_opy_ = test.parent
        if hook_name in [bstack111111l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪ᫭"), bstack111111l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧ᫮"), bstack111111l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭᫯"), bstack111111l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ᫰")]:
            bstack11l11l1l11l_opy_ = test
        scope = []
        while bstack11l11l1l11l_opy_ is not None:
            scope.append(bstack11l11l1l11l_opy_.name)
            bstack11l11l1l11l_opy_ = bstack11l11l1l11l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1lll1_opy_(hook_type):
        if hook_type == bstack111111l_opy_ (u"ࠤࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠢ᫱"):
            return bstack111111l_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢ࡫ࡳࡴࡱࠢ᫲")
        elif hook_type == bstack111111l_opy_ (u"ࠦࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠣ᫳"):
            return bstack111111l_opy_ (u"࡚ࠧࡥࡢࡴࡧࡳࡼࡴࠠࡩࡱࡲ࡯ࠧ᫴")
    @staticmethod
    def bstack11l11l1ll11_opy_(bstack1llllll1l_opy_):
        try:
            if not bstack1ll1l1ll_opy_.on():
                return bstack1llllll1l_opy_
            if os.environ.get(bstack111111l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠦ᫵"), None) == bstack111111l_opy_ (u"ࠢࡵࡴࡸࡩࠧ᫶"):
                tests = os.environ.get(bstack111111l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠧ᫷"), None)
                if tests is None or tests == bstack111111l_opy_ (u"ࠤࡱࡹࡱࡲࠢ᫸"):
                    return bstack1llllll1l_opy_
                bstack1llllll1l_opy_ = tests.split(bstack111111l_opy_ (u"ࠪ࠰ࠬ᫹"))
                return bstack1llllll1l_opy_
        except Exception as exc:
            logger.debug(bstack111111l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡶࡪࡸࡵ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡴ࠽ࠤࠧ᫺") + str(str(exc)) + bstack111111l_opy_ (u"ࠧࠨ᫻"))
        return bstack1llllll1l_opy_