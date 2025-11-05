# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import threading
from bstack_utils.helper import bstack11l1ll11l_opy_
from bstack_utils.constants import bstack11l11ll1l11_opy_, EVENTS, STAGE
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l11l1l1_opy_:
    bstack11l111l1l1l_opy_ = None
    @classmethod
    def bstack1l1l11l1ll_opy_(cls):
        if cls.on() and os.getenv(bstack11ll1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᬱ")):
            logger.info(
                bstack11ll1ll_opy_ (u"࡛ࠫ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠫᬲ").format(os.getenv(bstack11ll1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᬳ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖ᬴ࠪ"), None) is None or os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᬵ")] == bstack11ll1ll_opy_ (u"ࠣࡰࡸࡰࡱࠨᬶ"):
            return False
        return True
    @classmethod
    def bstack11l111l1lll_opy_(cls, bs_config, framework=bstack11ll1ll_opy_ (u"ࠤࠥᬷ")):
        bstack11ll11l11l1_opy_ = False
        for fw in bstack11l11ll1l11_opy_:
            if fw in framework:
                bstack11ll11l11l1_opy_ = True
        return bstack11l1ll11l_opy_(bs_config.get(bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᬸ"), bstack11ll11l11l1_opy_))
    @classmethod
    def bstack11l111ll1ll_opy_(cls, framework):
        return framework in bstack11l11ll1l11_opy_
    @classmethod
    def bstack11l111ll1l1_opy_(cls, bs_config, framework):
        return cls.bstack11l111l1lll_opy_(bs_config, framework) is True and cls.bstack11l111ll1ll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᬹ"), None)
    @staticmethod
    def bstack1l11111l_opy_():
        if getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᬺ"), None):
            return {
                bstack11ll1ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᬻ"): bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࠬᬼ"),
                bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᬽ"): getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᬾ"), None)
            }
        if getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᬿ"), None):
            return {
                bstack11ll1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩᭀ"): bstack11ll1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᭁ"),
                bstack11ll1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᭂ"): getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᭃ"), None)
            }
        return None
    @staticmethod
    def bstack11l111ll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11l1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l111111_opy_(test, hook_name=None):
        bstack11l111ll11l_opy_ = test.parent
        if hook_name in [bstack11ll1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ᭄࠭"), bstack11ll1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᭅ"), bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᭆ"), bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ᭇ")]:
            bstack11l111ll11l_opy_ = test
        scope = []
        while bstack11l111ll11l_opy_ is not None:
            scope.append(bstack11l111ll11l_opy_.name)
            bstack11l111ll11l_opy_ = bstack11l111ll11l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l111lll11_opy_(hook_type):
        if hook_type == bstack11ll1ll_opy_ (u"ࠧࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠥᭈ"):
            return bstack11ll1ll_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡮࡯ࡰ࡭ࠥᭉ")
        elif hook_type == bstack11ll1ll_opy_ (u"ࠢࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠦᭊ"):
            return bstack11ll1ll_opy_ (u"ࠣࡖࡨࡥࡷࡪ࡯ࡸࡰࠣ࡬ࡴࡵ࡫ࠣᭋ")
    @staticmethod
    def bstack11l111l1ll1_opy_(bstack111l1111_opy_):
        try:
            if not bstack1l11l1l1_opy_.on():
                return bstack111l1111_opy_
            if os.environ.get(bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠢᭌ"), None) == bstack11ll1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣ᭍"):
                tests = os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠣ᭎"), None)
                if tests is None or tests == bstack11ll1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ᭏"):
                    return bstack111l1111_opy_
                bstack111l1111_opy_ = tests.split(bstack11ll1ll_opy_ (u"࠭ࠬࠨ᭐"))
                return bstack111l1111_opy_
        except Exception as exc:
            logger.debug(bstack11ll1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡴࡸࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡀࠠࠣ᭑") + str(str(exc)) + bstack11ll1ll_opy_ (u"ࠣࠤ᭒"))
        return bstack111l1111_opy_