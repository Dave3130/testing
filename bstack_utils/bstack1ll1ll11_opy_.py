# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import threading
from bstack_utils.helper import bstack1111l11l1l_opy_
from bstack_utils.constants import bstack11l1l111lll_opy_, EVENTS, STAGE
from bstack_utils.bstack11llll111l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11l1l_opy_:
    bstack11l11l111l1_opy_ = None
    @classmethod
    def bstack111l1l1l1_opy_(cls):
        if cls.on() and os.getenv(bstack1lllll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨᬅ")):
            logger.info(
                bstack1lllll1l_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠩᬆ").format(os.getenv(bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᬇ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᬈ"), None) is None or os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᬉ")] == bstack1lllll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬊ"):
            return False
        return True
    @classmethod
    def bstack11l111llll1_opy_(cls, bs_config, framework=bstack1lllll1l_opy_ (u"ࠢࠣᬋ")):
        bstack11ll11lll1l_opy_ = False
        for fw in bstack11l1l111lll_opy_:
            if fw in framework:
                bstack11ll11lll1l_opy_ = True
        return bstack1111l11l1l_opy_(bs_config.get(bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᬌ"), bstack11ll11lll1l_opy_))
    @classmethod
    def bstack11l11l11111_opy_(cls, framework):
        return framework in bstack11l1l111lll_opy_
    @classmethod
    def bstack11l111lllll_opy_(cls, bs_config, framework):
        return cls.bstack11l111llll1_opy_(bs_config, framework) is True and cls.bstack11l11l11111_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬍ"), None)
    @staticmethod
    def bstack1ll1ll1l_opy_():
        if getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬎ"), None):
            return {
                bstack1lllll1l_opy_ (u"ࠫࡹࡿࡰࡦࠩᬏ"): bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࠪᬐ"),
                bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᬑ"): getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᬒ"), None)
            }
        if getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬓ"), None):
            return {
                bstack1lllll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᬔ"): bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᬕ"),
                bstack1lllll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᬖ"): getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬗ"), None)
            }
        return None
    @staticmethod
    def bstack11l11l11l11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll11l1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1ll11111_opy_(test, hook_name=None):
        bstack11l11l1111l_opy_ = test.parent
        if hook_name in [bstack1lllll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫᬘ"), bstack1lllll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᬙ"), bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬚ"), bstack1lllll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᬛ")]:
            bstack11l11l1111l_opy_ = test
        scope = []
        while bstack11l11l1111l_opy_ is not None:
            scope.append(bstack11l11l1111l_opy_.name)
            bstack11l11l1111l_opy_ = bstack11l11l1111l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l11l1l_opy_(hook_type):
        if hook_type == bstack1lllll1l_opy_ (u"ࠥࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠣᬜ"):
            return bstack1lllll1l_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣ࡬ࡴࡵ࡫ࠣᬝ")
        elif hook_type == bstack1lllll1l_opy_ (u"ࠧࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠤᬞ"):
            return bstack1lllll1l_opy_ (u"ࠨࡔࡦࡣࡵࡨࡴࡽ࡮ࠡࡪࡲࡳࡰࠨᬟ")
    @staticmethod
    def bstack11l11l111ll_opy_(bstack1lll11ll1_opy_):
        try:
            if not bstack1ll11l1l_opy_.on():
                return bstack1lll11ll1_opy_
            if os.environ.get(bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠧᬠ"), None) == bstack1lllll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᬡ"):
                tests = os.environ.get(bstack1lllll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘࠨᬢ"), None)
                if tests is None or tests == bstack1lllll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᬣ"):
                    return bstack1lll11ll1_opy_
                bstack1lll11ll1_opy_ = tests.split(bstack1lllll1l_opy_ (u"ࠫ࠱࠭ᬤ"))
                return bstack1lll11ll1_opy_
        except Exception as exc:
            logger.debug(bstack1lllll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷ࡫ࡲࡶࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵ࠾ࠥࠨᬥ") + str(str(exc)) + bstack1lllll1l_opy_ (u"ࠨࠢᬦ"))
        return bstack1lll11ll1_opy_