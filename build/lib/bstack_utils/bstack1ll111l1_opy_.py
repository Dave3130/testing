# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import threading
from bstack_utils.helper import bstack1l11l1ll1l_opy_
from bstack_utils.constants import bstack11l1l11l111_opy_, EVENTS, STAGE
from bstack_utils.bstack111ll1l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack11lll1l1_opy_:
    bstack11l11l1llll_opy_ = None
    @classmethod
    def bstack1l1ll11111_opy_(cls):
        if cls.on() and os.getenv(bstack1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᫧")):
            logger.info(
                bstack1l_opy_ (u"ࠧࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠧ᫨").format(os.getenv(bstack1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᫩"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᫪"), None) is None or os.environ[bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ᫫")] == bstack1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ᫬"):
            return False
        return True
    @classmethod
    def bstack11l11l1ll1l_opy_(cls, bs_config, framework=bstack1l_opy_ (u"ࠧࠨ᫭")):
        bstack11ll1l11ll1_opy_ = False
        for fw in bstack11l1l11l111_opy_:
            if fw in framework:
                bstack11ll1l11ll1_opy_ = True
        return bstack1l11l1ll1l_opy_(bs_config.get(bstack1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᫮"), bstack11ll1l11ll1_opy_))
    @classmethod
    def bstack11l11ll1111_opy_(cls, framework):
        return framework in bstack11l1l11l111_opy_
    @classmethod
    def bstack11l11l1ll11_opy_(cls, bs_config, framework):
        return cls.bstack11l11l1ll1l_opy_(bs_config, framework) is True and cls.bstack11l11ll1111_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ᫯"), None)
    @staticmethod
    def bstack1ll1llll_opy_():
        if getattr(threading.current_thread(), bstack1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ᫰"), None):
            return {
                bstack1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ᫱"): bstack1l_opy_ (u"ࠪࡸࡪࡹࡴࠨ᫲"),
                bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᫳"): getattr(threading.current_thread(), bstack1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ᫴"), None)
            }
        if getattr(threading.current_thread(), bstack1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ᫵"), None):
            return {
                bstack1l_opy_ (u"ࠧࡵࡻࡳࡩࠬ᫶"): bstack1l_opy_ (u"ࠨࡪࡲࡳࡰ࠭᫷"),
                bstack1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᫸"): getattr(threading.current_thread(), bstack1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ᫹"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1lll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11lll1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1lll1lll_opy_(test, hook_name=None):
        bstack11l11l1l11l_opy_ = test.parent
        if hook_name in [bstack1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩ᫺"), bstack1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭᫻"), bstack1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᫼"), bstack1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᫽")]:
            bstack11l11l1l11l_opy_ = test
        scope = []
        while bstack11l11l1l11l_opy_ is not None:
            scope.append(bstack11l11l1l11l_opy_.name)
            bstack11l11l1l11l_opy_ = bstack11l11l1l11l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1l1ll_opy_(hook_type):
        if hook_type == bstack1l_opy_ (u"ࠣࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍࠨ᫾"):
            return bstack1l_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡪࡲࡳࡰࠨ᫿")
        elif hook_type == bstack1l_opy_ (u"ࠥࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠢᬀ"):
            return bstack1l_opy_ (u"࡙ࠦ࡫ࡡࡳࡦࡲࡻࡳࠦࡨࡰࡱ࡮ࠦᬁ")
    @staticmethod
    def bstack11l11l1l1l1_opy_(bstack11l11l1l_opy_):
        try:
            if not bstack11lll1l1_opy_.on():
                return bstack11l11l1l_opy_
            if os.environ.get(bstack1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠥᬂ"), None) == bstack1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᬃ"):
                tests = os.environ.get(bstack1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠦᬄ"), None)
                if tests is None or tests == bstack1l_opy_ (u"ࠣࡰࡸࡰࡱࠨᬅ"):
                    return bstack11l11l1l_opy_
                bstack11l11l1l_opy_ = tests.split(bstack1l_opy_ (u"ࠩ࠯ࠫᬆ"))
                return bstack11l11l1l_opy_
        except Exception as exc:
            logger.debug(bstack1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡵࡩࡷࡻ࡮ࠡࡪࡤࡲࡩࡲࡥࡳ࠼ࠣࠦᬇ") + str(str(exc)) + bstack1l_opy_ (u"ࠦࠧᬈ"))
        return bstack11l11l1l_opy_