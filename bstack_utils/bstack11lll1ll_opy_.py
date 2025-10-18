# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import threading
from bstack_utils.helper import bstack1l1lll1ll1_opy_
from bstack_utils.constants import bstack11l11ll1lll_opy_, EVENTS, STAGE
from bstack_utils.bstack11l111l1ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lll1lll_opy_:
    bstack11l11l111l1_opy_ = None
    @classmethod
    def bstack1l1l1ll1l1_opy_(cls):
        if cls.on() and os.getenv(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᬇ")):
            logger.info(
                bstack11l111_opy_ (u"࡛ࠫ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠫᬈ").format(os.getenv(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᬉ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᬊ"), None) is None or os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᬋ")] == bstack11l111_opy_ (u"ࠣࡰࡸࡰࡱࠨᬌ"):
            return False
        return True
    @classmethod
    def bstack11l11l11l1l_opy_(cls, bs_config, framework=bstack11l111_opy_ (u"ࠤࠥᬍ")):
        bstack11ll11lll11_opy_ = False
        for fw in bstack11l11ll1lll_opy_:
            if fw in framework:
                bstack11ll11lll11_opy_ = True
        return bstack1l1lll1ll1_opy_(bs_config.get(bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᬎ"), bstack11ll11lll11_opy_))
    @classmethod
    def bstack11l11l11111_opy_(cls, framework):
        return framework in bstack11l11ll1lll_opy_
    @classmethod
    def bstack11l11l11l11_opy_(cls, bs_config, framework):
        return cls.bstack11l11l11l1l_opy_(bs_config, framework) is True and cls.bstack11l11l11111_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬏ"), None)
    @staticmethod
    def bstack11lll1l1_opy_():
        if getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᬐ"), None):
            return {
                bstack11l111_opy_ (u"࠭ࡴࡺࡲࡨࠫᬑ"): bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࠬᬒ"),
                bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᬓ"): getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᬔ"), None)
            }
        if getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᬕ"), None):
            return {
                bstack11l111_opy_ (u"ࠫࡹࡿࡰࡦࠩᬖ"): bstack11l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᬗ"),
                bstack11l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᬘ"): getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᬙ"), None)
            }
        return None
    @staticmethod
    def bstack11l111llll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lll1lll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1l1l11_opy_(test, hook_name=None):
        bstack11l111lllll_opy_ = test.parent
        if hook_name in [bstack11l111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᬚ"), bstack11l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᬛ"), bstack11l111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᬜ"), bstack11l111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ᬝ")]:
            bstack11l111lllll_opy_ = test
        scope = []
        while bstack11l111lllll_opy_ is not None:
            scope.append(bstack11l111lllll_opy_.name)
            bstack11l111lllll_opy_ = bstack11l111lllll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l111ll_opy_(hook_type):
        if hook_type == bstack11l111_opy_ (u"ࠧࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠥᬞ"):
            return bstack11l111_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡮࡯ࡰ࡭ࠥᬟ")
        elif hook_type == bstack11l111_opy_ (u"ࠢࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠦᬠ"):
            return bstack11l111_opy_ (u"ࠣࡖࡨࡥࡷࡪ࡯ࡸࡰࠣ࡬ࡴࡵ࡫ࠣᬡ")
    @staticmethod
    def bstack11l11l1111l_opy_(bstack1llll1l11_opy_):
        try:
            if not bstack1lll1lll_opy_.on():
                return bstack1llll1l11_opy_
            if os.environ.get(bstack11l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠢᬢ"), None) == bstack11l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᬣ"):
                tests = os.environ.get(bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠣᬤ"), None)
                if tests is None or tests == bstack11l111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᬥ"):
                    return bstack1llll1l11_opy_
                bstack1llll1l11_opy_ = tests.split(bstack11l111_opy_ (u"࠭ࠬࠨᬦ"))
                return bstack1llll1l11_opy_
        except Exception as exc:
            logger.debug(bstack11l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡴࡸࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡀࠠࠣᬧ") + str(str(exc)) + bstack11l111_opy_ (u"ࠣࠤᬨ"))
        return bstack1llll1l11_opy_