# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lllll11l1l_opy_,
)
from bstack_utils.helper import  bstack1lll111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111lll_opy_, bstack1lll1lll1l1_opy_, bstack1lll1lll11l_opy_, bstack1ll111lll11_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11ll11l111_opy_ import bstack11l1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll11_opy_ import bstack1lll11l11l1_opy_
from bstack_utils.percy import bstack11lll11l1_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11llll111_opy_(bstack1llllll111l_opy_):
    def __init__(self, bstack11llllllll1_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llllllll1_opy_ = bstack11llllllll1_opy_
        self.percy = bstack11lll11l1_opy_()
        self.bstack11l11l111l_opy_ = bstack11l1l1111_opy_()
        self.bstack1l111111111_opy_()
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.PRE), self.bstack11lllll1lll_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1ll1ll_opy_(self, instance: bstack1lllll11l1l_opy_, driver: object):
        bstack1l11l1l1lll_opy_ = TestFramework.bstack1l11l1111l1_opy_(instance.context)
        for t in bstack1l11l1l1lll_opy_:
            bstack1lll11l1111_opy_ = TestFramework.get_state(t, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l1111_opy_) or instance == driver:
                return t
    def bstack11lllll1lll_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llllll11ll_opy_.bstack1l1lll111l1_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_, 0)
            bstack1ll11l11lll_opy_ = self.bstack1l11l1ll1ll_opy_(instance, driver)
            bstack11lllllllll_opy_ = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1ll11ll11l1_opy_, None)
            if not bstack11lllllllll_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡶࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡡࡴࠢࡶࡩࡸࡹࡩࡰࡰࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡽࡪࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠣᔏ"))
                return
            driver_command = f.bstack1l1llll11l1_opy_(*args)
            for command in bstack1l1l1l1lll_opy_:
                if command == driver_command:
                    self.bstack111l111l11_opy_(driver, platform_index)
            bstack1lll11l11l_opy_ = self.percy.bstack111lll1l11_opy_()
            if driver_command in bstack11ll1lllll_opy_[bstack1lll11l11l_opy_]:
                self.bstack11l11l111l_opy_.bstack1l1llll1l1_opy_(bstack11lllllllll_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡪࡸࡲࡰࡴࠥᔐ"), e)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
        bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔑ") + str(kwargs) + bstack111111l_opy_ (u"ࠦࠧᔒ"))
            return
        if len(bstack1lll11l1111_opy_) > 1:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᔓ") + str(kwargs) + bstack111111l_opy_ (u"ࠨࠢᔔ"))
        bstack1lll111llll_opy_, bstack1lll1l111l1_opy_ = bstack1lll11l1111_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack111111l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᔕ") + str(kwargs) + bstack111111l_opy_ (u"ࠣࠤᔖ"))
            return
        bstack11llllll111_opy_ = {
            TestFramework.bstack1ll11lll111_opy_: bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᔗ"),
            TestFramework.bstack1llll11lll1_opy_: bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࠡࡷࡸ࡭ࡩࠨᔘ"),
            TestFramework.bstack1ll11ll11l1_opy_: bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡵࡩࡷࡻ࡮ࠡࡰࡤࡱࡪࠨᔙ")
        }
        bstack11llllll1l1_opy_ = { key: f.get_state(instance, key) for key in bstack11llllll111_opy_ }
        bstack11lllllll11_opy_ = [key for key, value in bstack11llllll1l1_opy_.items() if not value]
        if bstack11lllllll11_opy_:
            for key in bstack11lllllll11_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠣᔚ") + str(key) + bstack111111l_opy_ (u"ࠨࠢᔛ"))
            return
        platform_index = f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_, 0)
        if self.bstack11llllllll1_opy_.percy_capture_mode == bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᔜ"):
            bstack11l1l11ll_opy_ = bstack11llllll1l1_opy_.get(TestFramework.bstack1ll11ll11l1_opy_) + bstack111111l_opy_ (u"ࠣ࠯ࡷࡩࡸࡺࡣࡢࡵࡨࠦᔝ")
            bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack11lllllll1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l1l11ll_opy_,
                bstack1l1l1ll1l_opy_=bstack11llllll1l1_opy_[TestFramework.bstack1ll11lll111_opy_],
                bstack11ll11lll_opy_=bstack11llllll1l1_opy_[TestFramework.bstack1llll11lll1_opy_],
                bstack11llllll1l_opy_=platform_index
            )
            bstack1llllll1lll_opy_.end(EVENTS.bstack11lllllll1l_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᔞ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᔟ"), True, None, None, None, None, test_name=bstack11l1l11ll_opy_)
    def bstack111l111l11_opy_(self, driver, platform_index):
        if self.bstack11l11l111l_opy_.bstack1111ll1l1l_opy_() is True or self.bstack11l11l111l_opy_.capturing() is True:
            return
        self.bstack11l11l111l_opy_.bstack1l1lllllll_opy_()
        while not self.bstack11l11l111l_opy_.bstack1111ll1l1l_opy_():
            bstack11lllllllll_opy_ = self.bstack11l11l111l_opy_.bstack1lllll1l11_opy_()
            self.bstack1l1ll11l1_opy_(driver, bstack11lllllllll_opy_, platform_index)
        self.bstack11l11l111l_opy_.bstack1111lll111_opy_()
    def bstack1l1ll11l1_opy_(self, driver, bstack11llllll11_opy_, platform_index, test=None):
        from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
        bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack111ll1111l_opy_.value)
        if test != None:
            bstack1l1l1ll1l_opy_ = getattr(test, bstack111111l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᔠ"), None)
            bstack11ll11lll_opy_ = getattr(test, bstack111111l_opy_ (u"ࠬࡻࡵࡪࡦࠪᔡ"), None)
            PercySDK.screenshot(driver, bstack11llllll11_opy_, bstack1l1l1ll1l_opy_=bstack1l1l1ll1l_opy_, bstack11ll11lll_opy_=bstack11ll11lll_opy_, bstack11llllll1l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11llllll11_opy_)
        bstack1llllll1lll_opy_.end(EVENTS.bstack111ll1111l_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᔢ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᔣ"), True, None, None, None, None, test_name=bstack11llllll11_opy_)
    def bstack1l111111111_opy_(self):
        os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᔤ")] = str(self.bstack11llllllll1_opy_.success)
        os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ᔥ")] = str(self.bstack11llllllll1_opy_.percy_capture_mode)
        self.percy.bstack11llllll1ll_opy_(self.bstack11llllllll1_opy_.is_percy_auto_enabled)
        self.percy.bstack11llllll11l_opy_(self.bstack11llllllll1_opy_.percy_build_id)