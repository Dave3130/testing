# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
import threading
from bstack_utils.helper import bstack1ll11lll11_opy_
from bstack_utils.constants import bstack11l11ll11ll_opy_, EVENTS, STAGE
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack11llll1l_opy_:
    bstack11l111ll111_opy_ = None
    @classmethod
    def bstack11ll1lllll_opy_(cls):
        if cls.on() and os.getenv(bstack11l1111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢᬰ")):
            logger.info(
                bstack11l1111_opy_ (u"࡚ࠪ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠪᬱ").format(os.getenv(bstack11l1111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᬲ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᬳ"), None) is None or os.environ[bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖ᬴ࠪ")] == bstack11l1111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᬵ"):
            return False
        return True
    @classmethod
    def bstack11l111l1l1l_opy_(cls, bs_config, framework=bstack11l1111_opy_ (u"ࠣࠤᬶ")):
        bstack11ll11l1l11_opy_ = False
        for fw in bstack11l11ll11ll_opy_:
            if fw in framework:
                bstack11ll11l1l11_opy_ = True
        return bstack1ll11lll11_opy_(bs_config.get(bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᬷ"), bstack11ll11l1l11_opy_))
    @classmethod
    def bstack11l111l1lll_opy_(cls, framework):
        return framework in bstack11l11ll11ll_opy_
    @classmethod
    def bstack11l111l1ll1_opy_(cls, bs_config, framework):
        return cls.bstack11l111l1l1l_opy_(bs_config, framework) is True and cls.bstack11l111l1lll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᬸ"), None)
    @staticmethod
    def bstack1llll111_opy_():
        if getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᬹ"), None):
            return {
                bstack11l1111_opy_ (u"ࠬࡺࡹࡱࡧࠪᬺ"): bstack11l1111_opy_ (u"࠭ࡴࡦࡵࡷࠫᬻ"),
                bstack11l1111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬼ"): getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᬽ"), None)
            }
        if getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬾ"), None):
            return {
                bstack11l1111_opy_ (u"ࠪࡸࡾࡶࡥࠨᬿ"): bstack11l1111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᭀ"),
                bstack11l1111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᭁ"): getattr(threading.current_thread(), bstack11l1111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᭂ"), None)
            }
        return None
    @staticmethod
    def bstack11l111ll11l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11llll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1lll1ll1_opy_(test, hook_name=None):
        bstack11l111ll1l1_opy_ = test.parent
        if hook_name in [bstack11l1111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᭃ"), bstack11l1111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴ᭄ࠩ"), bstack11l1111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᭅ"), bstack11l1111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᭆ")]:
            bstack11l111ll1l1_opy_ = test
        scope = []
        while bstack11l111ll1l1_opy_ is not None:
            scope.append(bstack11l111ll1l1_opy_.name)
            bstack11l111ll1l1_opy_ = bstack11l111ll1l1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l111lll11_opy_(hook_type):
        if hook_type == bstack11l1111_opy_ (u"ࠦࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠤᭇ"):
            return bstack11l1111_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡭ࡵ࡯࡬ࠤᭈ")
        elif hook_type == bstack11l1111_opy_ (u"ࠨࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠥᭉ"):
            return bstack11l1111_opy_ (u"ࠢࡕࡧࡤࡶࡩࡵࡷ࡯ࠢ࡫ࡳࡴࡱࠢᭊ")
    @staticmethod
    def bstack11l111ll1ll_opy_(bstack11111l1l_opy_):
        try:
            if not bstack11llll1l_opy_.on():
                return bstack11111l1l_opy_
            if os.environ.get(bstack11l1111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࠨᭋ"), None) == bstack11l1111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᭌ"):
                tests = os.environ.get(bstack11l1111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠢ᭍"), None)
                if tests is None or tests == bstack11l1111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ᭎"):
                    return bstack11111l1l_opy_
                bstack11111l1l_opy_ = tests.split(bstack11l1111_opy_ (u"ࠬ࠲ࠧ᭏"))
                return bstack11111l1l_opy_
        except Exception as exc:
            logger.debug(bstack11l1111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡸࡥࡳࡷࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠿ࠦࠢ᭐") + str(str(exc)) + bstack11l1111_opy_ (u"ࠢࠣ᭑"))
        return bstack11111l1l_opy_