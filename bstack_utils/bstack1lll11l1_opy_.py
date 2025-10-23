# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import threading
from bstack_utils.helper import bstack11lllll1l1_opy_
from bstack_utils.constants import bstack11l11lll1ll_opy_, EVENTS, STAGE
from bstack_utils.bstack1l1l1llll1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11l11_opy_:
    bstack11l111lllll_opy_ = None
    @classmethod
    def bstack1lll1ll1ll_opy_(cls):
        if cls.on() and os.getenv(bstack11lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᬁ")):
            logger.info(
                bstack11lll1_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬᬂ").format(os.getenv(bstack11lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦᬃ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᬄ"), None) is None or os.environ[bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᬅ")] == bstack11lll1_opy_ (u"ࠤࡱࡹࡱࡲࠢᬆ"):
            return False
        return True
    @classmethod
    def bstack11l11l111l1_opy_(cls, bs_config, framework=bstack11lll1_opy_ (u"ࠥࠦᬇ")):
        bstack11ll11lll11_opy_ = False
        for fw in bstack11l11lll1ll_opy_:
            if fw in framework:
                bstack11ll11lll11_opy_ = True
        return bstack11lllll1l1_opy_(bs_config.get(bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᬈ"), bstack11ll11lll11_opy_))
    @classmethod
    def bstack11l11l111ll_opy_(cls, framework):
        return framework in bstack11l11lll1ll_opy_
    @classmethod
    def bstack11l11l11l11_opy_(cls, bs_config, framework):
        return cls.bstack11l11l111l1_opy_(bs_config, framework) is True and cls.bstack11l11l111ll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬉ"), None)
    @staticmethod
    def bstack1llll1l1_opy_():
        if getattr(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᬊ"), None):
            return {
                bstack11lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬᬋ"): bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᬌ"),
                bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᬍ"): getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬎ"), None)
            }
        if getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬏ"), None):
            return {
                bstack11lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪᬐ"): bstack11lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᬑ"),
                bstack11lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬒ"): getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬓ"), None)
            }
        return None
    @staticmethod
    def bstack11l111lll1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll11l11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1ll11l_opy_(test, hook_name=None):
        bstack11l111llll1_opy_ = test.parent
        if hook_name in [bstack11lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᬔ"), bstack11lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬕ"), bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᬖ"), bstack11lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬗ")]:
            bstack11l111llll1_opy_ = test
        scope = []
        while bstack11l111llll1_opy_ is not None:
            scope.append(bstack11l111llll1_opy_.name)
            bstack11l111llll1_opy_ = bstack11l111llll1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l11111_opy_(hook_type):
        if hook_type == bstack11lll1_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦᬘ"):
            return bstack11lll1_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦᬙ")
        elif hook_type == bstack11lll1_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧᬚ"):
            return bstack11lll1_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤᬛ")
    @staticmethod
    def bstack11l11l1111l_opy_(bstack1llll1lll_opy_):
        try:
            if not bstack1ll11l11_opy_.on():
                return bstack1llll1lll_opy_
            if os.environ.get(bstack11lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᬜ"), None) == bstack11lll1_opy_ (u"ࠦࡹࡸࡵࡦࠤᬝ"):
                tests = os.environ.get(bstack11lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᬞ"), None)
                if tests is None or tests == bstack11lll1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬟ"):
                    return bstack1llll1lll_opy_
                bstack1llll1lll_opy_ = tests.split(bstack11lll1_opy_ (u"ࠧ࠭ࠩᬠ"))
                return bstack1llll1lll_opy_
        except Exception as exc:
            logger.debug(bstack11lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᬡ") + str(str(exc)) + bstack11lll1_opy_ (u"ࠤࠥᬢ"))
        return bstack1llll1lll_opy_