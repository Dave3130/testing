# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
import threading
from bstack_utils.helper import bstack1111ll111l_opy_
from bstack_utils.constants import bstack11l1l11ll11_opy_, EVENTS, STAGE
from bstack_utils.bstack111l11ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l1l11ll_opy_:
    bstack11l11l1111l_opy_ = None
    @classmethod
    def bstack1111ll11l_opy_(cls):
        if cls.on() and os.getenv(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᬁ")):
            logger.info(
                bstack11l1l11_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬᬂ").format(os.getenv(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦᬃ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᬄ"), None) is None or os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᬅ")] == bstack11l1l11_opy_ (u"ࠤࡱࡹࡱࡲࠢᬆ"):
            return False
        return True
    @classmethod
    def bstack11l11l111l1_opy_(cls, bs_config, framework=bstack11l1l11_opy_ (u"ࠥࠦᬇ")):
        bstack11ll11ll11l_opy_ = False
        for fw in bstack11l1l11ll11_opy_:
            if fw in framework:
                bstack11ll11ll11l_opy_ = True
        return bstack1111ll111l_opy_(bs_config.get(bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᬈ"), bstack11ll11ll11l_opy_))
    @classmethod
    def bstack11l111lll1l_opy_(cls, framework):
        return framework in bstack11l1l11ll11_opy_
    @classmethod
    def bstack11l11l11111_opy_(cls, bs_config, framework):
        return cls.bstack11l11l111l1_opy_(bs_config, framework) is True and cls.bstack11l111lll1l_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬉ"), None)
    @staticmethod
    def bstack1l111lll_opy_():
        if getattr(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᬊ"), None):
            return {
                bstack11l1l11_opy_ (u"ࠧࡵࡻࡳࡩࠬᬋ"): bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᬌ"),
                bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᬍ"): getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬎ"), None)
            }
        if getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬏ"), None):
            return {
                bstack11l1l11_opy_ (u"ࠬࡺࡹࡱࡧࠪᬐ"): bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᬑ"),
                bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬒ"): getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬓ"), None)
            }
        return None
    @staticmethod
    def bstack11l111lll11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l11ll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1ll1111l_opy_(test, hook_name=None):
        bstack11l111llll1_opy_ = test.parent
        if hook_name in [bstack11l1l11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᬔ"), bstack11l1l11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬕ"), bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᬖ"), bstack11l1l11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬗ")]:
            bstack11l111llll1_opy_ = test
        scope = []
        while bstack11l111llll1_opy_ is not None:
            scope.append(bstack11l111llll1_opy_.name)
            bstack11l111llll1_opy_ = bstack11l111llll1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l111ll_opy_(hook_type):
        if hook_type == bstack11l1l11_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦᬘ"):
            return bstack11l1l11_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦᬙ")
        elif hook_type == bstack11l1l11_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧᬚ"):
            return bstack11l1l11_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤᬛ")
    @staticmethod
    def bstack11l111lllll_opy_(bstack111111l1_opy_):
        try:
            if not bstack1l1l11ll_opy_.on():
                return bstack111111l1_opy_
            if os.environ.get(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᬜ"), None) == bstack11l1l11_opy_ (u"ࠦࡹࡸࡵࡦࠤᬝ"):
                tests = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᬞ"), None)
                if tests is None or tests == bstack11l1l11_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬟ"):
                    return bstack111111l1_opy_
                bstack111111l1_opy_ = tests.split(bstack11l1l11_opy_ (u"ࠧ࠭ࠩᬠ"))
                return bstack111111l1_opy_
        except Exception as exc:
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᬡ") + str(str(exc)) + bstack11l1l11_opy_ (u"ࠤࠥᬢ"))
        return bstack111111l1_opy_