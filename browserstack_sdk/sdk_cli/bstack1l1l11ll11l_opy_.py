# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll1l1_opy_ import (
    bstack1llll1lll1l_opy_,
    bstack1lllll1l1ll_opy_,
    bstack1lllllll1l1_opy_,
)
from bstack_utils.helper import  bstack1l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11l1l_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll11l1lll_opy_, bstack1lll1lll1ll_opy_, bstack1llll111111_opy_, bstack1ll111llll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l111l1ll_opy_ import bstack111l11llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1lll111lll1_opy_
from bstack_utils.percy import bstack1ll1111ll_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l111111l_opy_(bstack1lllll11lll_opy_):
    def __init__(self, bstack11lllll11l1_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll11l1_opy_ = bstack11lllll11l1_opy_
        self.percy = bstack1ll1111ll_opy_()
        self.bstack1llll11ll1_opy_ = bstack111l11llll_opy_()
        self.bstack11llll1ll1l_opy_()
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_, bstack1lllll1l1ll_opy_.PRE), self.bstack11lllll1111_opy_)
        TestFramework.bstack1lllllll111_opy_((bstack1lll11l1lll_opy_.TEST, bstack1llll111111_opy_.POST), self.bstack1lll1l11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11l111_opy_(self, instance: bstack1lllllll1l1_opy_, driver: object):
        bstack1l11l11l1ll_opy_ = TestFramework.bstack1l11l1111ll_opy_(instance.context)
        for t in bstack1l11l11l1ll_opy_:
            bstack1lll1111ll1_opy_ = TestFramework.get_state(t, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111ll1_opy_) or instance == driver:
                return t
    def bstack11lllll1111_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll11111_opy_.bstack1l1ll1lllll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11llll_opy_, 0)
            bstack1ll11ll11l1_opy_ = self.bstack1l11l11l111_opy_(instance, driver)
            bstack11llll1lll1_opy_ = TestFramework.get_state(bstack1ll11ll11l1_opy_, TestFramework.bstack1ll11ll111l_opy_, None)
            if not bstack11llll1lll1_opy_:
                self.logger.debug(bstack111l1l_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡴࡨࡸࡺࡸ࡮ࡪࡰࡪࠤࡦࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡ࡫ࡶࠤࡳࡵࡴࠡࡻࡨࡸࠥࡹࡴࡢࡴࡷࡩࡩࠨᔷ"))
                return
            driver_command = f.bstack1l1ll1ll11l_opy_(*args)
            for command in bstack11ll11111l_opy_:
                if command == driver_command:
                    self.bstack1lllll1111_opy_(driver, platform_index)
            bstack1l1ll1llll_opy_ = self.percy.bstack1l1ll1lll1_opy_()
            if driver_command in bstack11l1lllll_opy_[bstack1l1ll1llll_opy_]:
                self.bstack1llll11ll1_opy_.bstack111l11lll1_opy_(bstack11llll1lll1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡨࡶࡷࡵࡲࠣᔸ"), e)
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
        bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])
        if not bstack1lll1111ll1_opy_:
            self.logger.debug(bstack111l1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᔹ") + str(kwargs) + bstack111l1l_opy_ (u"ࠤࠥᔺ"))
            return
        if len(bstack1lll1111ll1_opy_) > 1:
            self.logger.debug(bstack111l1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔻ") + str(kwargs) + bstack111l1l_opy_ (u"ࠦࠧᔼ"))
        bstack1lll1111l1l_opy_, bstack1lll1lllll1_opy_ = bstack1lll1111ll1_opy_[0]
        driver = bstack1lll1111l1l_opy_()
        if not driver:
            self.logger.debug(bstack111l1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔽ") + str(kwargs) + bstack111l1l_opy_ (u"ࠨࠢᔾ"))
            return
        bstack11lllll11ll_opy_ = {
            TestFramework.bstack1ll1l1111ll_opy_: bstack111l1l_opy_ (u"ࠢࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᔿ"),
            TestFramework.bstack1lll1ll1lll_opy_: bstack111l1l_opy_ (u"ࠣࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᕀ"),
            TestFramework.bstack1ll11ll111l_opy_: bstack111l1l_opy_ (u"ࠤࡷࡩࡸࡺࠠࡳࡧࡵࡹࡳࠦ࡮ࡢ࡯ࡨࠦᕁ")
        }
        bstack11llll1llll_opy_ = { key: f.get_state(instance, key) for key in bstack11lllll11ll_opy_ }
        bstack11lllll1l1l_opy_ = [key for key, value in bstack11llll1llll_opy_.items() if not value]
        if bstack11lllll1l1l_opy_:
            for key in bstack11lllll1l1l_opy_:
                self.logger.debug(bstack111l1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࠨᕂ") + str(key) + bstack111l1l_opy_ (u"ࠦࠧᕃ"))
            return
        platform_index = f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11llll_opy_, 0)
        if self.bstack11lllll11l1_opy_.percy_capture_mode == bstack111l1l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕄ"):
            bstack1111ll111l_opy_ = bstack11llll1llll_opy_.get(TestFramework.bstack1ll11ll111l_opy_) + bstack111l1l_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᕅ")
            bstack1ll11l11lll_opy_ = bstack1llllll11ll_opy_.bstack1ll11lllll1_opy_(EVENTS.bstack11lllll111l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1111ll111l_opy_,
                bstack1l11ll1l1_opy_=bstack11llll1llll_opy_[TestFramework.bstack1ll1l1111ll_opy_],
                bstack11l1ll11l_opy_=bstack11llll1llll_opy_[TestFramework.bstack1lll1ll1lll_opy_],
                bstack1lll1ll1ll_opy_=platform_index
            )
            bstack1llllll11ll_opy_.end(EVENTS.bstack11lllll111l_opy_.value, bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᕆ"), bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᕇ"), True, None, None, None, None, test_name=bstack1111ll111l_opy_)
    def bstack1lllll1111_opy_(self, driver, platform_index):
        if self.bstack1llll11ll1_opy_.bstack11l111lll_opy_() is True or self.bstack1llll11ll1_opy_.capturing() is True:
            return
        self.bstack1llll11ll1_opy_.bstack1111l11ll1_opy_()
        while not self.bstack1llll11ll1_opy_.bstack11l111lll_opy_():
            bstack11llll1lll1_opy_ = self.bstack1llll11ll1_opy_.bstack11l1l1l1l_opy_()
            self.bstack1l1ll111l1_opy_(driver, bstack11llll1lll1_opy_, platform_index)
        self.bstack1llll11ll1_opy_.bstack111l1lll11_opy_()
    def bstack1l1ll111l1_opy_(self, driver, bstack11l1ll1l1_opy_, platform_index, test=None):
        from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
        bstack1ll11l11lll_opy_ = bstack1llllll11ll_opy_.bstack1ll11lllll1_opy_(EVENTS.bstack1111l1lll_opy_.value)
        if test != None:
            bstack1l11ll1l1_opy_ = getattr(test, bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᕈ"), None)
            bstack11l1ll11l_opy_ = getattr(test, bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᕉ"), None)
            PercySDK.screenshot(driver, bstack11l1ll1l1_opy_, bstack1l11ll1l1_opy_=bstack1l11ll1l1_opy_, bstack11l1ll11l_opy_=bstack11l1ll11l_opy_, bstack1lll1ll1ll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11l1ll1l1_opy_)
        bstack1llllll11ll_opy_.end(EVENTS.bstack1111l1lll_opy_.value, bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕊ"), bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕋ"), True, None, None, None, None, test_name=bstack11l1ll1l1_opy_)
    def bstack11llll1ll1l_opy_(self):
        os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᕌ")] = str(self.bstack11lllll11l1_opy_.success)
        os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᕍ")] = str(self.bstack11lllll11l1_opy_.percy_capture_mode)
        self.percy.bstack11lllll1l11_opy_(self.bstack11lllll11l1_opy_.is_percy_auto_enabled)
        self.percy.bstack11llll1ll11_opy_(self.bstack11lllll11l1_opy_.percy_build_id)