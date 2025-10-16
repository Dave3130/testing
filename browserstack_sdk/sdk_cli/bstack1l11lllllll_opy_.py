# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack111111l111_opy_,
)
from bstack_utils.helper import  bstack1llll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll1l_opy_, bstack1llll1l1l11_opy_, bstack1lll1llll1l_opy_, bstack1ll111l1l1l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack11ll1ll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11llll1_opy_
from bstack_utils.percy import bstack1l1lll11ll_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1ll1111_opy_(bstack1llll1llll1_opy_):
    def __init__(self, bstack11lllllllll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllllllll_opy_ = bstack11lllllllll_opy_
        self.percy = bstack1l1lll11ll_opy_()
        self.bstack1ll1ll1ll_opy_ = bstack11ll1ll1ll_opy_()
        self.bstack11llllll1ll_opy_()
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1l1111111l1_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l111l11_opy_(self, instance: bstack111111l111_opy_, driver: object):
        bstack1l11l1ll11l_opy_ = TestFramework.bstack1l11ll111ll_opy_(instance.context)
        for t in bstack1l11l1ll11l_opy_:
            bstack1lll11l1l11_opy_ = TestFramework.get_state(t, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l1l11_opy_) or instance == driver:
                return t
    def bstack1l1111111l1_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll1ll1l_opy_.bstack1l1lll11lll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_, 0)
            bstack1l1lllll1l1_opy_ = self.bstack1l11l111l11_opy_(instance, driver)
            bstack11lllllll11_opy_ = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1ll1111l1ll_opy_, None)
            if not bstack11lllllll11_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡧࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡼࡩࡹࠦࡳࡵࡣࡵࡸࡪࡪࠢᔜ"))
                return
            driver_command = f.bstack1l1llll11l1_opy_(*args)
            for command in bstack1ll1111ll_opy_:
                if command == driver_command:
                    self.bstack111l11l1l_opy_(driver, platform_index)
            bstack111l11l11l_opy_ = self.percy.bstack11ll1l1ll_opy_()
            if driver_command in bstack11l1ll11ll_opy_[bstack111l11l11l_opy_]:
                self.bstack1ll1ll1ll_opy_.bstack1lllllll1l_opy_(bstack11lllllll11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡩࡷࡸ࡯ࡳࠤᔝ"), e)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
        bstack1lll11l1l11_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll11l1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᔞ") + str(kwargs) + bstack1l_opy_ (u"ࠥࠦᔟ"))
            return
        if len(bstack1lll11l1l11_opy_) > 1:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔠ") + str(kwargs) + bstack1l_opy_ (u"ࠧࠨᔡ"))
        bstack1lll111ll11_opy_, bstack1llll1111ll_opy_ = bstack1lll11l1l11_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᔢ") + str(kwargs) + bstack1l_opy_ (u"ࠢࠣᔣ"))
            return
        bstack11lllllll1l_opy_ = {
            TestFramework.bstack1ll1l11lll1_opy_: bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᔤ"),
            TestFramework.bstack1llll11ll11_opy_: bstack1l_opy_ (u"ࠤࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧᔥ"),
            TestFramework.bstack1ll1111l1ll_opy_: bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࠡࡴࡨࡶࡺࡴࠠ࡯ࡣࡰࡩࠧᔦ")
        }
        bstack11llllllll1_opy_ = { key: f.get_state(instance, key) for key in bstack11lllllll1l_opy_ }
        bstack11llllll11l_opy_ = [key for key, value in bstack11llllllll1_opy_.items() if not value]
        if bstack11llllll11l_opy_:
            for key in bstack11llllll11l_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠢᔧ") + str(key) + bstack1l_opy_ (u"ࠧࠨᔨ"))
            return
        platform_index = f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_, 0)
        if self.bstack11lllllllll_opy_.percy_capture_mode == bstack1l_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᔩ"):
            bstack11lllllll_opy_ = bstack11llllllll1_opy_.get(TestFramework.bstack1ll1111l1ll_opy_) + bstack1l_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥᔪ")
            bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1l11111111l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11lllllll_opy_,
                bstack1111l1ll1_opy_=bstack11llllllll1_opy_[TestFramework.bstack1ll1l11lll1_opy_],
                bstack1111lllll_opy_=bstack11llllllll1_opy_[TestFramework.bstack1llll11ll11_opy_],
                bstack1111l11111_opy_=platform_index
            )
            bstack1llll1l1lll_opy_.end(EVENTS.bstack1l11111111l_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᔫ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᔬ"), True, None, None, None, None, test_name=bstack11lllllll_opy_)
    def bstack111l11l1l_opy_(self, driver, platform_index):
        if self.bstack1ll1ll1ll_opy_.bstack11l1llllll_opy_() is True or self.bstack1ll1ll1ll_opy_.capturing() is True:
            return
        self.bstack1ll1ll1ll_opy_.bstack11l1111lll_opy_()
        while not self.bstack1ll1ll1ll_opy_.bstack11l1llllll_opy_():
            bstack11lllllll11_opy_ = self.bstack1ll1ll1ll_opy_.bstack1lll111111_opy_()
            self.bstack111ll1ll1l_opy_(driver, bstack11lllllll11_opy_, platform_index)
        self.bstack1ll1ll1ll_opy_.bstack1l1l11111l_opy_()
    def bstack111ll1ll1l_opy_(self, driver, bstack11l1l1ll1l_opy_, platform_index, test=None):
        from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
        bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1111ll1ll1_opy_.value)
        if test != None:
            bstack1111l1ll1_opy_ = getattr(test, bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᔭ"), None)
            bstack1111lllll_opy_ = getattr(test, bstack1l_opy_ (u"ࠫࡺࡻࡩࡥࠩᔮ"), None)
            PercySDK.screenshot(driver, bstack11l1l1ll1l_opy_, bstack1111l1ll1_opy_=bstack1111l1ll1_opy_, bstack1111lllll_opy_=bstack1111lllll_opy_, bstack1111l11111_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11l1l1ll1l_opy_)
        bstack1llll1l1lll_opy_.end(EVENTS.bstack1111ll1ll1_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᔯ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᔰ"), True, None, None, None, None, test_name=bstack11l1l1ll1l_opy_)
    def bstack11llllll1ll_opy_(self):
        os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᔱ")] = str(self.bstack11lllllllll_opy_.success)
        os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᔲ")] = str(self.bstack11lllllllll_opy_.percy_capture_mode)
        self.percy.bstack11llllll1l1_opy_(self.bstack11lllllllll_opy_.is_percy_auto_enabled)
        self.percy.bstack1l111111111_opy_(self.bstack11lllllllll_opy_.percy_build_id)