# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
import threading
from bstack_utils.helper import bstack111llll1l_opy_
from bstack_utils.constants import bstack11l1l1111l1_opy_, EVENTS, STAGE
from bstack_utils.bstack11ll1111l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l11111l_opy_:
    bstack11l11l11111_opy_ = None
    @classmethod
    def bstack11ll11l111_opy_(cls):
        if cls.on() and os.getenv(bstack1lll11l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᬖ")):
            logger.info(
                bstack1lll11l_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬᬗ").format(os.getenv(bstack1lll11l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦᬘ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᬙ"), None) is None or os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᬚ")] == bstack1lll11l_opy_ (u"ࠤࡱࡹࡱࡲࠢᬛ"):
            return False
        return True
    @classmethod
    def bstack11l111lll1l_opy_(cls, bs_config, framework=bstack1lll11l_opy_ (u"ࠥࠦᬜ")):
        bstack11ll11l1ll1_opy_ = False
        for fw in bstack11l1l1111l1_opy_:
            if fw in framework:
                bstack11ll11l1ll1_opy_ = True
        return bstack111llll1l_opy_(bs_config.get(bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᬝ"), bstack11ll11l1ll1_opy_))
    @classmethod
    def bstack11l111lll11_opy_(cls, framework):
        return framework in bstack11l1l1111l1_opy_
    @classmethod
    def bstack11l111ll1l1_opy_(cls, bs_config, framework):
        return cls.bstack11l111lll1l_opy_(bs_config, framework) is True and cls.bstack11l111lll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᬞ"), None)
    @staticmethod
    def bstack1llll11l_opy_():
        if getattr(threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᬟ"), None):
            return {
                bstack1lll11l_opy_ (u"ࠧࡵࡻࡳࡩࠬᬠ"): bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᬡ"),
                bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᬢ"): getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᬣ"), None)
            }
        if getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬤ"), None):
            return {
                bstack1lll11l_opy_ (u"ࠬࡺࡹࡱࡧࠪᬥ"): bstack1lll11l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᬦ"),
                bstack1lll11l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬧ"): getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᬨ"), None)
            }
        return None
    @staticmethod
    def bstack11l111ll1ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11111l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1lll1lll_opy_(test, hook_name=None):
        bstack11l111llll1_opy_ = test.parent
        if hook_name in [bstack1lll11l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᬩ"), bstack1lll11l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬪ"), bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᬫ"), bstack1lll11l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬬ")]:
            bstack11l111llll1_opy_ = test
        scope = []
        while bstack11l111llll1_opy_ is not None:
            scope.append(bstack11l111llll1_opy_.name)
            bstack11l111llll1_opy_ = bstack11l111llll1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l111lllll_opy_(hook_type):
        if hook_type == bstack1lll11l_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦᬭ"):
            return bstack1lll11l_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦᬮ")
        elif hook_type == bstack1lll11l_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧᬯ"):
            return bstack1lll11l_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤᬰ")
    @staticmethod
    def bstack11l111ll11l_opy_(bstack1llll111l_opy_):
        try:
            if not bstack1l11111l_opy_.on():
                return bstack1llll111l_opy_
            if os.environ.get(bstack1lll11l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᬱ"), None) == bstack1lll11l_opy_ (u"ࠦࡹࡸࡵࡦࠤᬲ"):
                tests = os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᬳ"), None)
                if tests is None or tests == bstack1lll11l_opy_ (u"ࠨ࡮ࡶ࡮࡯᬴ࠦ"):
                    return bstack1llll111l_opy_
                bstack1llll111l_opy_ = tests.split(bstack1lll11l_opy_ (u"ࠧ࠭ࠩᬵ"))
                return bstack1llll111l_opy_
        except Exception as exc:
            logger.debug(bstack1lll11l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᬶ") + str(str(exc)) + bstack1lll11l_opy_ (u"ࠤࠥᬷ"))
        return bstack1llll111l_opy_