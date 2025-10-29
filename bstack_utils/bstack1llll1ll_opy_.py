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
import os
import threading
from bstack_utils.helper import bstack1ll11lll11_opy_
from bstack_utils.constants import bstack11l11llllll_opy_, EVENTS, STAGE
from bstack_utils.bstack1l11111111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1llll_opy_:
    bstack11l111lll11_opy_ = None
    @classmethod
    def bstack1l11l1ll1l_opy_(cls):
        if cls.on() and os.getenv(bstack11ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨᬡ")):
            logger.info(
                bstack11ll1l_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠩᬢ").format(os.getenv(bstack11ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᬣ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᬤ"), None) is None or os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᬥ")] == bstack11ll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬦ"):
            return False
        return True
    @classmethod
    def bstack11l111lll1l_opy_(cls, bs_config, framework=bstack11ll1l_opy_ (u"ࠢࠣᬧ")):
        bstack11ll11ll11l_opy_ = False
        for fw in bstack11l11llllll_opy_:
            if fw in framework:
                bstack11ll11ll11l_opy_ = True
        return bstack1ll11lll11_opy_(bs_config.get(bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᬨ"), bstack11ll11ll11l_opy_))
    @classmethod
    def bstack11l111llll1_opy_(cls, framework):
        return framework in bstack11l11llllll_opy_
    @classmethod
    def bstack11l111ll1ll_opy_(cls, bs_config, framework):
        return cls.bstack11l111lll1l_opy_(bs_config, framework) is True and cls.bstack11l111llll1_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬩ"), None)
    @staticmethod
    def bstack1ll1l1ll_opy_():
        if getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬪ"), None):
            return {
                bstack11ll1l_opy_ (u"ࠫࡹࡿࡰࡦࠩᬫ"): bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࠪᬬ"),
                bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᬭ"): getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᬮ"), None)
            }
        if getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬯ"), None):
            return {
                bstack11ll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᬰ"): bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᬱ"),
                bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᬲ"): getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬳ"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1111l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1llll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1ll1lll1_opy_(test, hook_name=None):
        bstack11l111lllll_opy_ = test.parent
        if hook_name in [bstack11ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶ᬴ࠫ"), bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᬵ"), bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬶ"), bstack11ll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᬷ")]:
            bstack11l111lllll_opy_ = test
        scope = []
        while bstack11l111lllll_opy_ is not None:
            scope.append(bstack11l111lllll_opy_.name)
            bstack11l111lllll_opy_ = bstack11l111lllll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l111ll1l1_opy_(hook_type):
        if hook_type == bstack11ll1l_opy_ (u"ࠥࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠣᬸ"):
            return bstack11ll1l_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣ࡬ࡴࡵ࡫ࠣᬹ")
        elif hook_type == bstack11ll1l_opy_ (u"ࠧࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠤᬺ"):
            return bstack11ll1l_opy_ (u"ࠨࡔࡦࡣࡵࡨࡴࡽ࡮ࠡࡪࡲࡳࡰࠨᬻ")
    @staticmethod
    def bstack11l11l11111_opy_(bstack11111l11_opy_):
        try:
            if not bstack1ll1llll_opy_.on():
                return bstack11111l11_opy_
            if os.environ.get(bstack11ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠧᬼ"), None) == bstack11ll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᬽ"):
                tests = os.environ.get(bstack11ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘࠨᬾ"), None)
                if tests is None or tests == bstack11ll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᬿ"):
                    return bstack11111l11_opy_
                bstack11111l11_opy_ = tests.split(bstack11ll1l_opy_ (u"ࠫ࠱࠭ᭀ"))
                return bstack11111l11_opy_
        except Exception as exc:
            logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷ࡫ࡲࡶࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵ࠾ࠥࠨᭁ") + str(str(exc)) + bstack11ll1l_opy_ (u"ࠨࠢᭂ"))
        return bstack11111l11_opy_