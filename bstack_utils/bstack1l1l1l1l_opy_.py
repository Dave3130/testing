# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import threading
from bstack_utils.helper import bstack1ll1111ll1_opy_
from bstack_utils.constants import bstack11l1l111111_opy_, EVENTS, STAGE
from bstack_utils.bstack1ll1111l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l111ll1_opy_:
    bstack11l11l111l1_opy_ = None
    @classmethod
    def bstack11ll11l1l1_opy_(cls):
        if cls.on() and os.getenv(bstack1l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᫺")):
            logger.info(
                bstack1l1_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ᫻").format(os.getenv(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᫼"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᫽"), None) is None or os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᫾")] == bstack1l1_opy_ (u"ࠤࡱࡹࡱࡲࠢ᫿"):
            return False
        return True
    @classmethod
    def bstack11l11l11l1l_opy_(cls, bs_config, framework=bstack1l1_opy_ (u"ࠥࠦᬀ")):
        bstack11ll11lll1l_opy_ = False
        for fw in bstack11l1l111111_opy_:
            if fw in framework:
                bstack11ll11lll1l_opy_ = True
        return bstack1ll1111ll1_opy_(bs_config.get(bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᬁ"), bstack11ll11lll1l_opy_))
    @classmethod
    def bstack11l11l11lll_opy_(cls, framework):
        return framework in bstack11l1l111111_opy_
    @classmethod
    def bstack11l11l11l11_opy_(cls, bs_config, framework):
        return cls.bstack11l11l11l1l_opy_(bs_config, framework) is True and cls.bstack11l11l11lll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬂ"), None)
    @staticmethod
    def bstack1l1llll1_opy_():
        if getattr(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᬃ"), None):
            return {
                bstack1l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᬄ"): bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᬅ"),
                bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᬆ"): getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬇ"), None)
            }
        if getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬈ"), None):
            return {
                bstack1l1_opy_ (u"ࠬࡺࡹࡱࡧࠪᬉ"): bstack1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᬊ"),
                bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬋ"): getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬌ"), None)
            }
        return None
    @staticmethod
    def bstack11l11l111ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l111ll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1ll11l11_opy_(test, hook_name=None):
        bstack11l11l11111_opy_ = test.parent
        if hook_name in [bstack1l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᬍ"), bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬎ"), bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᬏ"), bstack1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬐ")]:
            bstack11l11l11111_opy_ = test
        scope = []
        while bstack11l11l11111_opy_ is not None:
            scope.append(bstack11l11l11111_opy_.name)
            bstack11l11l11111_opy_ = bstack11l11l11111_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1111l_opy_(hook_type):
        if hook_type == bstack1l1_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦᬑ"):
            return bstack1l1_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦᬒ")
        elif hook_type == bstack1l1_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧᬓ"):
            return bstack1l1_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤᬔ")
    @staticmethod
    def bstack11l11l11ll1_opy_(bstack1lll1ll1l_opy_):
        try:
            if not bstack1l111ll1_opy_.on():
                return bstack1lll1ll1l_opy_
            if os.environ.get(bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᬕ"), None) == bstack1l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᬖ"):
                tests = os.environ.get(bstack1l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᬗ"), None)
                if tests is None or tests == bstack1l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬘ"):
                    return bstack1lll1ll1l_opy_
                bstack1lll1ll1l_opy_ = tests.split(bstack1l1_opy_ (u"ࠧ࠭ࠩᬙ"))
                return bstack1lll1ll1l_opy_
        except Exception as exc:
            logger.debug(bstack1l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᬚ") + str(str(exc)) + bstack1l1_opy_ (u"ࠤࠥᬛ"))
        return bstack1lll1ll1l_opy_