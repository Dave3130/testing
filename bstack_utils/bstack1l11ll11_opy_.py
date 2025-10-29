# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import threading
from bstack_utils.helper import bstack11lll1l11_opy_
from bstack_utils.constants import bstack11l1l1111ll_opy_, EVENTS, STAGE
from bstack_utils.bstack11l1l11ll1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l1l111l_opy_:
    bstack11l111ll1l1_opy_ = None
    @classmethod
    def bstack11llll1ll1_opy_(cls):
        if cls.on() and os.getenv(bstack11l11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨᬡ")):
            logger.info(
                bstack11l11ll_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠩᬢ").format(os.getenv(bstack11l11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᬣ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᬤ"), None) is None or os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᬥ")] == bstack11l11ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬦ"):
            return False
        return True
    @classmethod
    def bstack11l111lllll_opy_(cls, bs_config, framework=bstack11l11ll_opy_ (u"ࠢࠣᬧ")):
        bstack11ll11l1lll_opy_ = False
        for fw in bstack11l1l1111ll_opy_:
            if fw in framework:
                bstack11ll11l1lll_opy_ = True
        return bstack11lll1l11_opy_(bs_config.get(bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᬨ"), bstack11ll11l1lll_opy_))
    @classmethod
    def bstack11l11l11111_opy_(cls, framework):
        return framework in bstack11l1l1111ll_opy_
    @classmethod
    def bstack11l11l1111l_opy_(cls, bs_config, framework):
        return cls.bstack11l111lllll_opy_(bs_config, framework) is True and cls.bstack11l11l11111_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬩ"), None)
    @staticmethod
    def bstack1lll1lll_opy_():
        if getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬪ"), None):
            return {
                bstack11l11ll_opy_ (u"ࠫࡹࡿࡰࡦࠩᬫ"): bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࠪᬬ"),
                bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᬭ"): getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᬮ"), None)
            }
        if getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬯ"), None):
            return {
                bstack11l11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᬰ"): bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᬱ"),
                bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᬲ"): getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬳ"), None)
            }
        return None
    @staticmethod
    def bstack11l111ll1ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l111l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l111l1l_opy_(test, hook_name=None):
        bstack11l111lll1l_opy_ = test.parent
        if hook_name in [bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶ᬴ࠫ"), bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᬵ"), bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬶ"), bstack11l11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᬷ")]:
            bstack11l111lll1l_opy_ = test
        scope = []
        while bstack11l111lll1l_opy_ is not None:
            scope.append(bstack11l111lll1l_opy_.name)
            bstack11l111lll1l_opy_ = bstack11l111lll1l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l111lll11_opy_(hook_type):
        if hook_type == bstack11l11ll_opy_ (u"ࠥࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠣᬸ"):
            return bstack11l11ll_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣ࡬ࡴࡵ࡫ࠣᬹ")
        elif hook_type == bstack11l11ll_opy_ (u"ࠧࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠤᬺ"):
            return bstack11l11ll_opy_ (u"ࠨࡔࡦࡣࡵࡨࡴࡽ࡮ࠡࡪࡲࡳࡰࠨᬻ")
    @staticmethod
    def bstack11l111llll1_opy_(bstack1111l111_opy_):
        try:
            if not bstack1l1l111l_opy_.on():
                return bstack1111l111_opy_
            if os.environ.get(bstack11l11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠧᬼ"), None) == bstack11l11ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᬽ"):
                tests = os.environ.get(bstack11l11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘࠨᬾ"), None)
                if tests is None or tests == bstack11l11ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᬿ"):
                    return bstack1111l111_opy_
                bstack1111l111_opy_ = tests.split(bstack11l11ll_opy_ (u"ࠫ࠱࠭ᭀ"))
                return bstack1111l111_opy_
        except Exception as exc:
            logger.debug(bstack11l11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷ࡫ࡲࡶࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵ࠾ࠥࠨᭁ") + str(str(exc)) + bstack11l11ll_opy_ (u"ࠨࠢᭂ"))
        return bstack1111l111_opy_