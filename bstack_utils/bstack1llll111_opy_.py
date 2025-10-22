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
import os
import threading
from bstack_utils.helper import bstack11l1llll1_opy_
from bstack_utils.constants import bstack11l11ll1111_opy_, EVENTS, STAGE
from bstack_utils.bstack1l11l1lll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lll1111_opy_:
    bstack11l11l11111_opy_ = None
    @classmethod
    def bstack11l11l1l1l_opy_(cls):
        if cls.on() and os.getenv(bstack111l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᬂ")):
            logger.info(
                bstack111l1l_opy_ (u"࠭ࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳ࠭ᬃ").format(os.getenv(bstack111l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᬄ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᬅ"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᬆ")] == bstack111l1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᬇ"):
            return False
        return True
    @classmethod
    def bstack11l111lll1l_opy_(cls, bs_config, framework=bstack111l1l_opy_ (u"ࠦࠧᬈ")):
        bstack11ll11ll1l1_opy_ = False
        for fw in bstack11l11ll1111_opy_:
            if fw in framework:
                bstack11ll11ll1l1_opy_ = True
        return bstack11l1llll1_opy_(bs_config.get(bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᬉ"), bstack11ll11ll1l1_opy_))
    @classmethod
    def bstack11l111lll11_opy_(cls, framework):
        return framework in bstack11l11ll1111_opy_
    @classmethod
    def bstack11l111lllll_opy_(cls, bs_config, framework):
        return cls.bstack11l111lll1l_opy_(bs_config, framework) is True and cls.bstack11l111lll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᬊ"), None)
    @staticmethod
    def bstack1ll11111_opy_():
        if getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᬋ"), None):
            return {
                bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᬌ"): bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࠧᬍ"),
                bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᬎ"): getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᬏ"), None)
            }
        if getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬐ"), None):
            return {
                bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫᬑ"): bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᬒ"),
                bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᬓ"): getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬔ"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1111l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lll1111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l11l11l_opy_(test, hook_name=None):
        bstack11l11l111l1_opy_ = test.parent
        if hook_name in [bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᬕ"), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᬖ"), bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᬗ"), bstack111l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᬘ")]:
            bstack11l11l111l1_opy_ = test
        scope = []
        while bstack11l11l111l1_opy_ is not None:
            scope.append(bstack11l11l111l1_opy_.name)
            bstack11l11l111l1_opy_ = bstack11l11l111l1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l111ll_opy_(hook_type):
        if hook_type == bstack111l1l_opy_ (u"ࠢࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠧᬙ"):
            return bstack111l1l_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡩࡱࡲ࡯ࠧᬚ")
        elif hook_type == bstack111l1l_opy_ (u"ࠤࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍࠨᬛ"):
            return bstack111l1l_opy_ (u"ࠥࡘࡪࡧࡲࡥࡱࡺࡲࠥ࡮࡯ࡰ࡭ࠥᬜ")
    @staticmethod
    def bstack11l111llll1_opy_(bstack111ll1l1_opy_):
        try:
            if not bstack1lll1111_opy_.on():
                return bstack111ll1l1_opy_
            if os.environ.get(bstack111l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠤᬝ"), None) == bstack111l1l_opy_ (u"ࠧࡺࡲࡶࡧࠥᬞ"):
                tests = os.environ.get(bstack111l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠥᬟ"), None)
                if tests is None or tests == bstack111l1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᬠ"):
                    return bstack111ll1l1_opy_
                bstack111ll1l1_opy_ = tests.split(bstack111l1l_opy_ (u"ࠨ࠮ࠪᬡ"))
                return bstack111ll1l1_opy_
        except Exception as exc:
            logger.debug(bstack111l1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡨࡶࡺࡴࠠࡩࡣࡱࡨࡱ࡫ࡲ࠻ࠢࠥᬢ") + str(str(exc)) + bstack111l1l_opy_ (u"ࠥࠦᬣ"))
        return bstack111ll1l1_opy_