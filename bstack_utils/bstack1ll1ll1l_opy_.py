# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import threading
from bstack_utils.helper import bstack111lll11l1_opy_
from bstack_utils.constants import bstack11l1l11llll_opy_, EVENTS, STAGE
from bstack_utils.bstack11111l1l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1l1_opy_:
    bstack11l11l11l1l_opy_ = None
    @classmethod
    def bstack11lllll1l1_opy_(cls):
        if cls.on() and os.getenv(bstack11l11l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᫺")):
            logger.info(
                bstack11l11l1_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ᫻").format(os.getenv(bstack11l11l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᫼"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᫽"), None) is None or os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᫾")] == bstack11l11l1_opy_ (u"ࠤࡱࡹࡱࡲࠢ᫿"):
            return False
        return True
    @classmethod
    def bstack11l11l11ll1_opy_(cls, bs_config, framework=bstack11l11l1_opy_ (u"ࠥࠦᬀ")):
        bstack11ll11lllll_opy_ = False
        for fw in bstack11l1l11llll_opy_:
            if fw in framework:
                bstack11ll11lllll_opy_ = True
        return bstack111lll11l1_opy_(bs_config.get(bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᬁ"), bstack11ll11lllll_opy_))
    @classmethod
    def bstack11l11l11lll_opy_(cls, framework):
        return framework in bstack11l1l11llll_opy_
    @classmethod
    def bstack11l11l11111_opy_(cls, bs_config, framework):
        return cls.bstack11l11l11ll1_opy_(bs_config, framework) is True and cls.bstack11l11l11lll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬂ"), None)
    @staticmethod
    def bstack1l11111l_opy_():
        if getattr(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᬃ"), None):
            return {
                bstack11l11l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᬄ"): bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᬅ"),
                bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᬆ"): getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬇ"), None)
            }
        if getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬈ"), None):
            return {
                bstack11l11l1_opy_ (u"ࠬࡺࡹࡱࡧࠪᬉ"): bstack11l11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᬊ"),
                bstack11l11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬋ"): getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬌ"), None)
            }
        return None
    @staticmethod
    def bstack11l11l111ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1lll1l_opy_(test, hook_name=None):
        bstack11l11l111l1_opy_ = test.parent
        if hook_name in [bstack11l11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᬍ"), bstack11l11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬎ"), bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᬏ"), bstack11l11l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬐ")]:
            bstack11l11l111l1_opy_ = test
        scope = []
        while bstack11l11l111l1_opy_ is not None:
            scope.append(bstack11l11l111l1_opy_.name)
            bstack11l11l111l1_opy_ = bstack11l11l111l1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1111l_opy_(hook_type):
        if hook_type == bstack11l11l1_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦᬑ"):
            return bstack11l11l1_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦᬒ")
        elif hook_type == bstack11l11l1_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧᬓ"):
            return bstack11l11l1_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤᬔ")
    @staticmethod
    def bstack11l11l11l11_opy_(bstack111l111l_opy_):
        try:
            if not bstack1ll1l1l1_opy_.on():
                return bstack111l111l_opy_
            if os.environ.get(bstack11l11l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᬕ"), None) == bstack11l11l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᬖ"):
                tests = os.environ.get(bstack11l11l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᬗ"), None)
                if tests is None or tests == bstack11l11l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬘ"):
                    return bstack111l111l_opy_
                bstack111l111l_opy_ = tests.split(bstack11l11l1_opy_ (u"ࠧ࠭ࠩᬙ"))
                return bstack111l111l_opy_
        except Exception as exc:
            logger.debug(bstack11l11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᬚ") + str(str(exc)) + bstack11l11l1_opy_ (u"ࠤࠥᬛ"))
        return bstack111l111l_opy_