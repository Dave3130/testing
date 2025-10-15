# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import threading
from bstack_utils.helper import bstack1lll1ll111_opy_
from bstack_utils.constants import bstack11l11ll1l11_opy_, EVENTS, STAGE
from bstack_utils.bstack1ll1ll111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l11llll_opy_:
    bstack11l11l1lll1_opy_ = None
    @classmethod
    def bstack1l11l1ll11_opy_(cls):
        if cls.on() and os.getenv(bstack1ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᫟")):
            logger.info(
                bstack1ll1l_opy_ (u"࠭ࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳ࠭᫠").format(os.getenv(bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧ᫡"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᫢"), None) is None or os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᫣")] == bstack1ll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ᫤"):
            return False
        return True
    @classmethod
    def bstack11l11l1ll1l_opy_(cls, bs_config, framework=bstack1ll1l_opy_ (u"ࠦࠧ᫥")):
        bstack11ll1l11l11_opy_ = False
        for fw in bstack11l11ll1l11_opy_:
            if fw in framework:
                bstack11ll1l11l11_opy_ = True
        return bstack1lll1ll111_opy_(bs_config.get(bstack1ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᫦"), bstack11ll1l11l11_opy_))
    @classmethod
    def bstack11l11l1l111_opy_(cls, framework):
        return framework in bstack11l11ll1l11_opy_
    @classmethod
    def bstack11l11l1l1l1_opy_(cls, bs_config, framework):
        return cls.bstack11l11l1ll1l_opy_(bs_config, framework) is True and cls.bstack11l11l1l111_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ᫧"), None)
    @staticmethod
    def bstack1l1ll1ll_opy_():
        if getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ᫨"), None):
            return {
                bstack1ll1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭᫩"): bstack1ll1l_opy_ (u"ࠩࡷࡩࡸࡺࠧ᫪"),
                bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᫫"): getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ᫬"), None)
            }
        if getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᫭"), None):
            return {
                bstack1ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ᫮"): bstack1ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ᫯"),
                bstack1ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᫰"): getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭᫱"), None)
            }
        return None
    @staticmethod
    def bstack11l11l11lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11llll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l111lll_opy_(test, hook_name=None):
        bstack11l11l1l1ll_opy_ = test.parent
        if hook_name in [bstack1ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ᫲"), bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ᫳"), bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫ᫴"), bstack1ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨ᫵")]:
            bstack11l11l1l1ll_opy_ = test
        scope = []
        while bstack11l11l1l1ll_opy_ is not None:
            scope.append(bstack11l11l1l1ll_opy_.name)
            bstack11l11l1l1ll_opy_ = bstack11l11l1l1ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1ll11_opy_(hook_type):
        if hook_type == bstack1ll1l_opy_ (u"ࠢࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠧ᫶"):
            return bstack1ll1l_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡩࡱࡲ࡯ࠧ᫷")
        elif hook_type == bstack1ll1l_opy_ (u"ࠤࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍࠨ᫸"):
            return bstack1ll1l_opy_ (u"ࠥࡘࡪࡧࡲࡥࡱࡺࡲࠥ࡮࡯ࡰ࡭ࠥ᫹")
    @staticmethod
    def bstack11l11l1l11l_opy_(bstack1lllll11l_opy_):
        try:
            if not bstack1l11llll_opy_.on():
                return bstack1lllll11l_opy_
            if os.environ.get(bstack1ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠤ᫺"), None) == bstack1ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥ᫻"):
                tests = os.environ.get(bstack1ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠥ᫼"), None)
                if tests is None or tests == bstack1ll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ᫽"):
                    return bstack1lllll11l_opy_
                bstack1lllll11l_opy_ = tests.split(bstack1ll1l_opy_ (u"ࠨ࠮ࠪ᫾"))
                return bstack1lllll11l_opy_
        except Exception as exc:
            logger.debug(bstack1ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡨࡶࡺࡴࠠࡩࡣࡱࡨࡱ࡫ࡲ࠻ࠢࠥ᫿") + str(str(exc)) + bstack1ll1l_opy_ (u"ࠥࠦᬀ"))
        return bstack1lllll11l_opy_