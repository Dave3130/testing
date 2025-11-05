# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
import threading
from bstack_utils.helper import bstack1l1111l1ll_opy_
from bstack_utils.constants import bstack11l11ll1lll_opy_, EVENTS, STAGE
from bstack_utils.bstack111111l11l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l11lll1_opy_:
    bstack11l111ll11l_opy_ = None
    @classmethod
    def bstack1lll1ll1l1_opy_(cls):
        if cls.on() and os.getenv(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢᬰ")):
            logger.info(
                bstack11111_opy_ (u"࡚ࠪ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠪᬱ").format(os.getenv(bstack11111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᬲ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᬳ"), None) is None or os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖ᬴ࠪ")] == bstack11111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᬵ"):
            return False
        return True
    @classmethod
    def bstack11l111l1lll_opy_(cls, bs_config, framework=bstack11111_opy_ (u"ࠣࠤᬶ")):
        bstack11ll11l11l1_opy_ = False
        for fw in bstack11l11ll1lll_opy_:
            if fw in framework:
                bstack11ll11l11l1_opy_ = True
        return bstack1l1111l1ll_opy_(bs_config.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᬷ"), bstack11ll11l11l1_opy_))
    @classmethod
    def bstack11l111lll11_opy_(cls, framework):
        return framework in bstack11l11ll1lll_opy_
    @classmethod
    def bstack11l111ll1l1_opy_(cls, bs_config, framework):
        return cls.bstack11l111l1lll_opy_(bs_config, framework) is True and cls.bstack11l111lll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᬸ"), None)
    @staticmethod
    def bstack11lll11l_opy_():
        if getattr(threading.current_thread(), bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᬹ"), None):
            return {
                bstack11111_opy_ (u"ࠬࡺࡹࡱࡧࠪᬺ"): bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࠫᬻ"),
                bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᬼ"): getattr(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᬽ"), None)
            }
        if getattr(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᬾ"), None):
            return {
                bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨᬿ"): bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᭀ"),
                bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᭁ"): getattr(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᭂ"), None)
            }
        return None
    @staticmethod
    def bstack11l111l1l1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11lll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1lllll11_opy_(test, hook_name=None):
        bstack11l111l1ll1_opy_ = test.parent
        if hook_name in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᭃ"), bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴ᭄ࠩ"), bstack11111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᭅ"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᭆ")]:
            bstack11l111l1ll1_opy_ = test
        scope = []
        while bstack11l111l1ll1_opy_ is not None:
            scope.append(bstack11l111l1ll1_opy_.name)
            bstack11l111l1ll1_opy_ = bstack11l111l1ll1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l111ll111_opy_(hook_type):
        if hook_type == bstack11111_opy_ (u"ࠦࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠤᭇ"):
            return bstack11111_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡭ࡵ࡯࡬ࠤᭈ")
        elif hook_type == bstack11111_opy_ (u"ࠨࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠥᭉ"):
            return bstack11111_opy_ (u"ࠢࡕࡧࡤࡶࡩࡵࡷ࡯ࠢ࡫ࡳࡴࡱࠢᭊ")
    @staticmethod
    def bstack11l111ll1ll_opy_(bstack111lll1l_opy_):
        try:
            if not bstack1l11lll1_opy_.on():
                return bstack111lll1l_opy_
            if os.environ.get(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࠨᭋ"), None) == bstack11111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᭌ"):
                tests = os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠢ᭍"), None)
                if tests is None or tests == bstack11111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ᭎"):
                    return bstack111lll1l_opy_
                bstack111lll1l_opy_ = tests.split(bstack11111_opy_ (u"ࠬ࠲ࠧ᭏"))
                return bstack111lll1l_opy_
        except Exception as exc:
            logger.debug(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡸࡥࡳࡷࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠿ࠦࠢ᭐") + str(str(exc)) + bstack11111_opy_ (u"ࠢࠣ᭑"))
        return bstack111lll1l_opy_