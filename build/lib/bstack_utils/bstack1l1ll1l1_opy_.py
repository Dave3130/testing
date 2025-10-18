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
import os
import threading
from bstack_utils.helper import bstack1lll1l1lll_opy_
from bstack_utils.constants import bstack11l11ll11l1_opy_, EVENTS, STAGE
from bstack_utils.bstack11l1l1l1ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l1l111l_opy_:
    bstack11l11l11l11_opy_ = None
    @classmethod
    def bstack1111l1ll1_opy_(cls):
        if cls.on() and os.getenv(bstack11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᬉ")):
            logger.info(
                bstack11ll_opy_ (u"࠭ࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳ࠭ᬊ").format(os.getenv(bstack11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᬋ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᬌ"), None) is None or os.environ[bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᬍ")] == bstack11ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᬎ"):
            return False
        return True
    @classmethod
    def bstack11l111lll1l_opy_(cls, bs_config, framework=bstack11ll_opy_ (u"ࠦࠧᬏ")):
        bstack11ll11ll1ll_opy_ = False
        for fw in bstack11l11ll11l1_opy_:
            if fw in framework:
                bstack11ll11ll1ll_opy_ = True
        return bstack1lll1l1lll_opy_(bs_config.get(bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᬐ"), bstack11ll11ll1ll_opy_))
    @classmethod
    def bstack11l111lllll_opy_(cls, framework):
        return framework in bstack11l11ll11l1_opy_
    @classmethod
    def bstack11l11l11111_opy_(cls, bs_config, framework):
        return cls.bstack11l111lll1l_opy_(bs_config, framework) is True and cls.bstack11l111lllll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᬑ"), None)
    @staticmethod
    def bstack1ll11l11_opy_():
        if getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᬒ"), None):
            return {
                bstack11ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᬓ"): bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᬔ"),
                bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᬕ"): getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᬖ"), None)
            }
        if getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬗ"), None):
            return {
                bstack11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᬘ"): bstack11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᬙ"),
                bstack11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᬚ"): getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬛ"), None)
            }
        return None
    @staticmethod
    def bstack11l111llll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l111l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l11ll11_opy_(test, hook_name=None):
        bstack11l11l111ll_opy_ = test.parent
        if hook_name in [bstack11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᬜ"), bstack11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᬝ"), bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᬞ"), bstack11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᬟ")]:
            bstack11l11l111ll_opy_ = test
        scope = []
        while bstack11l11l111ll_opy_ is not None:
            scope.append(bstack11l11l111ll_opy_.name)
            bstack11l11l111ll_opy_ = bstack11l11l111ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l111l1_opy_(hook_type):
        if hook_type == bstack11ll_opy_ (u"ࠢࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠧᬠ"):
            return bstack11ll_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡩࡱࡲ࡯ࠧᬡ")
        elif hook_type == bstack11ll_opy_ (u"ࠤࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍࠨᬢ"):
            return bstack11ll_opy_ (u"ࠥࡘࡪࡧࡲࡥࡱࡺࡲࠥ࡮࡯ࡰ࡭ࠥᬣ")
    @staticmethod
    def bstack11l11l1111l_opy_(bstack111ll111_opy_):
        try:
            if not bstack1l1l111l_opy_.on():
                return bstack111ll111_opy_
            if os.environ.get(bstack11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠤᬤ"), None) == bstack11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᬥ"):
                tests = os.environ.get(bstack11ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠥᬦ"), None)
                if tests is None or tests == bstack11ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᬧ"):
                    return bstack111ll111_opy_
                bstack111ll111_opy_ = tests.split(bstack11ll_opy_ (u"ࠨ࠮ࠪᬨ"))
                return bstack111ll111_opy_
        except Exception as exc:
            logger.debug(bstack11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡨࡶࡺࡴࠠࡩࡣࡱࡨࡱ࡫ࡲ࠻ࠢࠥᬩ") + str(str(exc)) + bstack11ll_opy_ (u"ࠥࠦᬪ"))
        return bstack111ll111_opy_