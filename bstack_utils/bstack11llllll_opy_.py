# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import threading
from bstack_utils.helper import bstack1lll1ll1l1_opy_
from bstack_utils.constants import bstack11l1l1ll1ll_opy_, EVENTS, STAGE
from bstack_utils.bstack1ll1111ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1ll_opy_:
    bstack11l11l1l1ll_opy_ = None
    @classmethod
    def bstack11llll11ll_opy_(cls):
        if cls.on() and os.getenv(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᫝")):
            logger.info(
                bstack11l1l11_opy_ (u"࡛ࠫ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠫ᫞").format(os.getenv(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᫟"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ᫠"), None) is None or os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᫡")] == bstack11l1l11_opy_ (u"ࠣࡰࡸࡰࡱࠨ᫢"):
            return False
        return True
    @classmethod
    def bstack11l11l11lll_opy_(cls, bs_config, framework=bstack11l1l11_opy_ (u"ࠤࠥ᫣")):
        bstack11ll1l11l11_opy_ = False
        for fw in bstack11l1l1ll1ll_opy_:
            if fw in framework:
                bstack11ll1l11l11_opy_ = True
        return bstack1lll1ll1l1_opy_(bs_config.get(bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ᫤"), bstack11ll1l11l11_opy_))
    @classmethod
    def bstack11l11l1ll11_opy_(cls, framework):
        return framework in bstack11l1l1ll1ll_opy_
    @classmethod
    def bstack11l11l1ll1l_opy_(cls, bs_config, framework):
        return cls.bstack11l11l11lll_opy_(bs_config, framework) is True and cls.bstack11l11l1ll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ᫥"), None)
    @staticmethod
    def bstack1ll11l11_opy_():
        if getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ᫦"), None):
            return {
                bstack11l1l11_opy_ (u"࠭ࡴࡺࡲࡨࠫ᫧"): bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࠬ᫨"),
                bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᫩"): getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᫪"), None)
            }
        if getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ᫫"), None):
            return {
                bstack11l1l11_opy_ (u"ࠫࡹࡿࡰࡦࠩ᫬"): bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ᫭"),
                bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᫮"): getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ᫯"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1lll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l1ll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1l1l1l_opy_(test, hook_name=None):
        bstack11l11l1l1l1_opy_ = test.parent
        if hook_name in [bstack11l1l11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭᫰"), bstack11l1l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ᫱"), bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩ᫲"), bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭᫳")]:
            bstack11l11l1l1l1_opy_ = test
        scope = []
        while bstack11l11l1l1l1_opy_ is not None:
            scope.append(bstack11l11l1l1l1_opy_.name)
            bstack11l11l1l1l1_opy_ = bstack11l11l1l1l1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1l111_opy_(hook_type):
        if hook_type == bstack11l1l11_opy_ (u"ࠧࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠥ᫴"):
            return bstack11l1l11_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡮࡯ࡰ࡭ࠥ᫵")
        elif hook_type == bstack11l1l11_opy_ (u"ࠢࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠦ᫶"):
            return bstack11l1l11_opy_ (u"ࠣࡖࡨࡥࡷࡪ࡯ࡸࡰࠣ࡬ࡴࡵ࡫ࠣ᫷")
    @staticmethod
    def bstack11l11l1l11l_opy_(bstack11l11lll_opy_):
        try:
            if not bstack1ll1l1ll_opy_.on():
                return bstack11l11lll_opy_
            if os.environ.get(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠢ᫸"), None) == bstack11l1l11_opy_ (u"ࠥࡸࡷࡻࡥࠣ᫹"):
                tests = os.environ.get(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠣ᫺"), None)
                if tests is None or tests == bstack11l1l11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ᫻"):
                    return bstack11l11lll_opy_
                bstack11l11lll_opy_ = tests.split(bstack11l1l11_opy_ (u"࠭ࠬࠨ᫼"))
                return bstack11l11lll_opy_
        except Exception as exc:
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡴࡸࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡀࠠࠣ᫽") + str(str(exc)) + bstack11l1l11_opy_ (u"ࠣࠤ᫾"))
        return bstack11l11lll_opy_