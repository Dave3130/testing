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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack111llll11l_opy_ import bstack1ll11l1l1ll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll11l11l_opy_,
    bstack1lll1l11111_opy_,
    bstack1lll11llll1_opy_,
    bstack1ll1l1l11l1_opy_,
    bstack1ll111ll111_opy_,
)
import traceback
from bstack_utils.helper import bstack1l1llll1111_opy_
from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll111ll11l_opy_ import bstack1ll11llllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1ll1_opy_ import bstack1lll11ll111_opy_
bstack1ll11lll11l_opy_ = bstack1l1llll1111_opy_()
bstack1ll1111llll_opy_ = bstack1l1_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤሎ")
bstack1ll11ll1ll1_opy_ = bstack1l1_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨሏ")
bstack1l1llll111l_opy_ = bstack1l1_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥሐ")
bstack1ll1l11l111_opy_ = 1.0
_1l1llll1lll_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll11ll1l11_opy_ = bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧሑ")
    bstack1ll11l111ll_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࠦሒ")
    bstack1ll1l111l1l_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨሓ")
    bstack1ll1l111ll1_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࠥሔ")
    bstack1ll1l1l1ll1_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧሕ")
    bstack1ll1l1ll1ll_opy_: bool
    bstack1lll11l1ll1_opy_: bstack1lll11ll111_opy_  = None
    bstack1ll11lll1ll_opy_ = [
        bstack1llll11l11l_opy_.BEFORE_ALL,
        bstack1llll11l11l_opy_.AFTER_ALL,
        bstack1llll11l11l_opy_.BEFORE_EACH,
        bstack1llll11l11l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11lllll1_opy_: Dict[str, str],
        bstack1ll11111ll1_opy_: List[str]=[bstack1l1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢሖ")],
        bstack1lll11l1ll1_opy_: bstack1lll11ll111_opy_ = None,
        bstack1llll1l11ll_opy_=None
    ):
        super().__init__(bstack1ll11111ll1_opy_, bstack1ll11lllll1_opy_, bstack1lll11l1ll1_opy_)
        self.bstack1ll1l1ll1ll_opy_ = any(bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣሗ") in item.lower() for item in bstack1ll11111ll1_opy_)
        self.bstack1llll1l11ll_opy_ = bstack1llll1l11ll_opy_
    def track_event(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll11l11l_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll11lll1ll_opy_:
            bstack1ll11l1l1ll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll11l11l_opy_.NONE:
            self.logger.warning(bstack1l1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࠨመ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠨࠢሙ"))
            return
        if not self.bstack1ll1l1ll1ll_opy_:
            self.logger.warning(bstack1l1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠽ࠣሚ") + str(str(self.bstack1ll11111ll1_opy_)) + bstack1l1_opy_ (u"ࠣࠤማ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦሜ") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦም"))
            return
        instance = self.__1ll111lll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡦࡸࡧࡴ࠿ࠥሞ") + str(args) + bstack1l1_opy_ (u"ࠧࠨሟ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11lll1ll_opy_ and test_hook_state == bstack1lll11llll1_opy_.PRE:
                bstack1ll11ll1lll_opy_ = bstack1lllllll11l_opy_.bstack1ll1l1l1lll_opy_(EVENTS.bstack1l1l1l11l_opy_.value)
                name = str(EVENTS.bstack1l1l1l11l_opy_.name)+bstack1l1_opy_ (u"ࠨ࠺ࠣሠ")+str(test_framework_state.name)
                TestFramework.bstack1ll11111l1l_opy_(instance, name, bstack1ll11ll1lll_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴࠣࡴࡷ࡫࠺ࠡࡽࢀࠦሡ").format(e))
        try:
            if test_framework_state == bstack1llll11l11l_opy_.TEST:
                if not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1111l1_opy_) and test_hook_state == bstack1lll11llll1_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11llll1l_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l1_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣሢ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠤࠥሣ"))
                if test_hook_state == bstack1lll11llll1_opy_.PRE and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11l1ll1l_opy_):
                    TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1ll11l1ll1l_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11l11ll1_opy_(instance, args)
                    self.logger.debug(bstack1l1_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣሤ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠦࠧሥ"))
                elif test_hook_state == bstack1lll11llll1_opy_.POST and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1lllllll1_opy_):
                    TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1l1lllllll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣሦ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠨࠢሧ"))
            elif test_framework_state == bstack1llll11l11l_opy_.STEP:
                if test_hook_state == bstack1lll11llll1_opy_.PRE:
                    PytestBDDFramework.__1ll111l1l1l_opy_(instance, args)
                elif test_hook_state == bstack1lll11llll1_opy_.POST:
                    PytestBDDFramework.__1l1lllll1ll_opy_(instance, args)
            elif test_framework_state == bstack1llll11l11l_opy_.LOG and test_hook_state == bstack1lll11llll1_opy_.POST:
                PytestBDDFramework.__1ll1l111111_opy_(instance, *args)
            elif test_framework_state == bstack1llll11l11l_opy_.LOG_REPORT and test_hook_state == bstack1lll11llll1_opy_.POST:
                self.__1ll111l1l11_opy_(instance, *args)
                self.__1ll11ll11ll_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll11lll1ll_opy_:
                self.__1ll1l11ll1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣረ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠣࠤሩ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11l1lll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11lll1ll_opy_ and test_hook_state == bstack1lll11llll1_opy_.POST:
                name = str(EVENTS.bstack1l1l1l11l_opy_.name)+bstack1l1_opy_ (u"ࠤ࠽ࠦሪ")+str(test_framework_state.name)
                bstack1ll11ll1lll_opy_ = TestFramework.bstack1ll111ll1l1_opy_(instance, name)
                bstack1lllllll11l_opy_.end(EVENTS.bstack1l1l1l11l_opy_.value, bstack1ll11ll1lll_opy_+bstack1l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥራ"), bstack1ll11ll1lll_opy_+bstack1l1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤሬ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧር").format(e))
    def bstack1l1lllll1l1_opy_(self):
        return self.bstack1ll1l1ll1ll_opy_
    def __1ll1111ll11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥሮ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l111l_opy_(rep, [bstack1l1_opy_ (u"ࠢࡸࡪࡨࡲࠧሯ"), bstack1l1_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤሰ"), bstack1l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤሱ"), bstack1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥሲ"), bstack1l1_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧሳ"), bstack1l1_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦሴ")])
        return None
    def __1ll111l1l11_opy_(self, instance: bstack1lll1l11111_opy_, *args):
        result = self.__1ll1111ll11_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111l111_opy_ = None
        if result.get(bstack1l1_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢስ"), None) == bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢሶ") and len(args) > 1 and getattr(args[1], bstack1l1_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤሷ"), None) is not None:
            failure = [{bstack1l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬሸ"): [args[1].excinfo.exconly(), result.get(bstack1l1_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤሹ"), None)]}]
            bstack111111l111_opy_ = bstack1l1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧሺ") if bstack1l1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣሻ") in getattr(args[1].excinfo, bstack1l1_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣሼ"), bstack1l1_opy_ (u"ࠢࠣሽ")) else bstack1l1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤሾ")
        bstack1ll111111ll_opy_ = result.get(bstack1l1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥሿ"), TestFramework.bstack1ll11l1ll11_opy_)
        if bstack1ll111111ll_opy_ != TestFramework.bstack1ll11l1ll11_opy_:
            TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1l1lllll11l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l11llll_opy_(instance, {
            TestFramework.bstack1lll1ll11l1_opy_: failure,
            TestFramework.bstack1ll11ll1111_opy_: bstack111111l111_opy_,
            TestFramework.bstack1lll1ll11ll_opy_: bstack1ll111111ll_opy_,
        })
    def __1ll111lll1l_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll11l11l_opy_.SETUP_FIXTURE:
            instance = self.__1ll11111l11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l1ll11l_opy_ bstack1ll11l1l11l_opy_ this to be bstack1l1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥቀ")
            if test_framework_state == bstack1llll11l11l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11llll11_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll11l11l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1_opy_ (u"ࠦࡳࡵࡤࡦࠤቁ"), None), bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧቂ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1_opy_ (u"ࠨ࡮ࡰࡦࡨࠦቃ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢቄ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll1l11l1l1_opy_(target) if target else None
        return instance
    def __1ll1l11ll1l_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1llllllll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l111ll_opy_, {})
        if not key in bstack1l1llllllll_opy_:
            bstack1l1llllllll_opy_[key] = []
        bstack1ll1111l1l1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l111l1l_opy_, {})
        if not key in bstack1ll1111l1l1_opy_:
            bstack1ll1111l1l1_opy_[key] = []
        bstack1ll111l111l_opy_ = {
            PytestBDDFramework.bstack1ll11l111ll_opy_: bstack1l1llllllll_opy_,
            PytestBDDFramework.bstack1ll1l111l1l_opy_: bstack1ll1111l1l1_opy_,
        }
        if test_hook_state == bstack1lll11llll1_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l1_opy_ (u"ࠣ࡭ࡨࡽࠧቅ"): key,
                TestFramework.bstack1ll1l111l11_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l1l111_opy_: TestFramework.bstack1ll1l11l1ll_opy_,
                TestFramework.bstack1ll1l11lll1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1111l1ll_opy_: [],
                TestFramework.bstack1l1llll11l1_opy_: hook_name,
                TestFramework.bstack1l1llllll1l_opy_: bstack1ll11llllll_opy_.bstack1l1llll1l11_opy_()
            }
            bstack1l1llllllll_opy_[key].append(hook)
            bstack1ll111l111l_opy_[PytestBDDFramework.bstack1ll1l111ll1_opy_] = key
        elif test_hook_state == bstack1lll11llll1_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1l1llllllll_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1ll1111ll11_opy_(*args)
                if result:
                    bstack1ll11ll1l1l_opy_ = result.get(bstack1l1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥቆ"), TestFramework.bstack1ll1l11l1ll_opy_)
                    if bstack1ll11ll1l1l_opy_ != TestFramework.bstack1ll1l11l1ll_opy_:
                        hook[TestFramework.bstack1ll11l1l111_opy_] = bstack1ll11ll1l1l_opy_
                hook[TestFramework.bstack1l1llllll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1l1llllll1l_opy_] = bstack1ll11llllll_opy_.bstack1l1llll1l11_opy_()
                self.bstack1ll1111l111_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l111l1_opy_, [])
                self.bstack1ll1111ll1l_opy_(instance, logs)
                bstack1ll1111l1l1_opy_[key].append(hook)
                bstack1ll111l111l_opy_[PytestBDDFramework.bstack1ll1l1l1ll1_opy_] = key
        TestFramework.bstack1ll1l11llll_opy_(instance, bstack1ll111l111l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤቇ") + str(bstack1ll1111l1l1_opy_) + bstack1l1_opy_ (u"ࠦࠧቈ"))
    def __1ll11111l11_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l111l_opy_(args[0], [bstack1l1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ቉"), bstack1l1_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢቊ"), bstack1l1_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢቋ"), bstack1l1_opy_ (u"ࠣ࡫ࡧࡷࠧቌ"), bstack1l1_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦቍ"), bstack1l1_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥ቎")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l1_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥ቏")) else fixturedef.get(bstack1l1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦቐ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦቑ")) else None
        node = request.node if hasattr(request, bstack1l1_opy_ (u"ࠢ࡯ࡱࡧࡩࠧቒ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣቓ")) else None
        baseid = fixturedef.get(bstack1l1_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤቔ"), None) or bstack1l1_opy_ (u"ࠥࠦቕ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤቖ")):
            target = PytestBDDFramework.__1ll1l11l11l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢ቗")) else None
            if target and not TestFramework.bstack1ll1l11l1l1_opy_(target):
                self.__1ll11llll11_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣቘ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠢࠣ቙"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨቚ") + str(target) + bstack1l1_opy_ (u"ࠤࠥቛ"))
            return None
        instance = TestFramework.bstack1ll1l11l1l1_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧቜ") + str(target) + bstack1l1_opy_ (u"ࠦࠧቝ"))
            return None
        bstack1ll11l11l1l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll1l11_opy_, {})
        if os.getenv(bstack1l1_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨ቞"), bstack1l1_opy_ (u"ࠨ࠱ࠣ቟")) == bstack1l1_opy_ (u"ࠢ࠲ࠤበ"):
            bstack1ll1l1111ll_opy_ = bstack1l1_opy_ (u"ࠣ࠼ࠥቡ").join((scope, fixturename))
            bstack1ll111l1lll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll111llll1_opy_ = {
                bstack1l1_opy_ (u"ࠤ࡮ࡩࡾࠨቢ"): bstack1ll1l1111ll_opy_,
                bstack1l1_opy_ (u"ࠥࡸࡦ࡭ࡳࠣባ"): PytestBDDFramework.__1ll11ll11l1_opy_(request.node, scenario),
                bstack1l1_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧቤ"): fixturedef,
                bstack1l1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦብ"): scope,
                bstack1l1_opy_ (u"ࠨࡴࡺࡲࡨࠦቦ"): None,
            }
            try:
                if test_hook_state == bstack1lll11llll1_opy_.POST and callable(getattr(args[-1], bstack1l1_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦቧ"), None)):
                    bstack1ll111llll1_opy_[bstack1l1_opy_ (u"ࠣࡶࡼࡴࡪࠨቨ")] = TestFramework.bstack1ll1l1l11ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11llll1_opy_.PRE:
                bstack1ll111llll1_opy_[bstack1l1_opy_ (u"ࠤࡸࡹ࡮ࡪࠢቩ")] = uuid4().__str__()
                bstack1ll111llll1_opy_[PytestBDDFramework.bstack1ll1l11lll1_opy_] = bstack1ll111l1lll_opy_
            elif test_hook_state == bstack1lll11llll1_opy_.POST:
                bstack1ll111llll1_opy_[PytestBDDFramework.bstack1l1llllll11_opy_] = bstack1ll111l1lll_opy_
            if bstack1ll1l1111ll_opy_ in bstack1ll11l11l1l_opy_:
                bstack1ll11l11l1l_opy_[bstack1ll1l1111ll_opy_].update(bstack1ll111llll1_opy_)
                self.logger.debug(bstack1l1_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦቪ") + str(bstack1ll11l11l1l_opy_[bstack1ll1l1111ll_opy_]) + bstack1l1_opy_ (u"ࠦࠧቫ"))
            else:
                bstack1ll11l11l1l_opy_[bstack1ll1l1111ll_opy_] = bstack1ll111llll1_opy_
                self.logger.debug(bstack1l1_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣቬ") + str(len(bstack1ll11l11l1l_opy_)) + bstack1l1_opy_ (u"ࠨࠢቭ"))
        TestFramework.bstack1llll1l1lll_opy_(instance, PytestBDDFramework.bstack1ll11ll1l11_opy_, bstack1ll11l11l1l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢቮ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠣࠤቯ"))
        return instance
    def __1ll11llll11_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        ob = bstack1lll1l11111_opy_(ctx, self.bstack1ll11111ll1_opy_, self.bstack1ll11lllll1_opy_, test_framework_state)
        TestFramework.bstack1ll1l11llll_opy_(ob, {
            TestFramework.bstack1lll1l1111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1ll1l11_opy_: context.test_framework_version,
            TestFramework.bstack1l1lll1llll_opy_: [],
            PytestBDDFramework.bstack1ll11ll1l11_opy_: {},
            PytestBDDFramework.bstack1ll1l111l1l_opy_: {},
            PytestBDDFramework.bstack1ll11l111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l1lll_opy_(ob, TestFramework.bstack1ll111111l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l1lll_opy_(ob, TestFramework.bstack1lllll1l11l_opy_, context.platform_index)
        TestFramework.bstack1lll1lllll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤተ") + str(TestFramework.bstack1lll1lllll1_opy_.keys()) + bstack1l1_opy_ (u"ࠥࠦቱ"))
        return ob
    @staticmethod
    def __1ll11l11ll1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1_opy_ (u"ࠫ࡮ࡪࠧቲ"): id(step),
                bstack1l1_opy_ (u"ࠬࡺࡥࡹࡶࠪታ"): step.name,
                bstack1l1_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧቴ"): step.keyword,
            })
        meta = {
            bstack1l1_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨት"): {
                bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ቶ"): feature.name,
                bstack1l1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧቷ"): feature.filename,
                bstack1l1_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨቸ"): feature.description
            },
            bstack1l1_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ቹ"): {
                bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪቺ"): scenario.name
            },
            bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬቻ"): steps,
            bstack1l1_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩቼ"): PytestBDDFramework.__1ll11l11lll_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll11l11l11_opy_: meta
            }
        )
    def bstack1ll1111l111_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡳࡪ࡯࡬ࡰࡦࡸࠠࡵࡱࠣࡸ࡭࡫ࠠࡋࡣࡹࡥࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫࡭ࡸࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡉࡨࡦࡥ࡮ࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡫ࡱࡷ࡮ࡪࡥࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠲࡙ࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡈࡲࡶࠥ࡫ࡡࡤࡪࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹࠬࠡࡴࡨࡴࡱࡧࡣࡦࡵ࡙ࠣࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥࠤ࡮ࡴࠠࡪࡶࡶࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡋࡩࠤࡦࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡪࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡮ࡣࡷࡧ࡭࡫ࡳࠡࡣࠣࡱࡴࡪࡩࡧ࡫ࡨࡨࠥ࡮࡯ࡰ࡭࠰ࡰࡪࡼࡥ࡭ࠢࡩ࡭ࡱ࡫ࠬࠡ࡫ࡷࠤࡨࡸࡥࡢࡶࡨࡷࠥࡧࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࠢࡺ࡭ࡹ࡮ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡘ࡯࡭ࡪ࡮ࡤࡶࡱࡿࠬࠡ࡫ࡷࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢ࡯ࡳࡨࡧࡴࡦࡦࠣ࡭ࡳࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡤࡼࠤࡷ࡫ࡰ࡭ࡣࡦ࡭ࡳ࡭ࠠࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧࠦࡷࡪࡶ࡫ࠤࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡕࡪࡨࠤࡨࡸࡥࡢࡶࡨࡨࠥࡒ࡯ࡨࡇࡱࡸࡷࡿࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡣࡵࡩࠥࡧࡤࡥࡧࡧࠤࡹࡵࠠࡵࡪࡨࠤ࡭ࡵ࡯࡬ࠩࡶࠤࠧࡲ࡯ࡨࡵࠥࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡪࡲࡳࡰࡀࠠࡕࡪࡨࠤࡪࡼࡥ࡯ࡶࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶࠤࡦࡴࡤࠡࡪࡲࡳࡰࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡗࡩࡸࡺࡌࡦࡸࡨࡰࠥࡳ࡯࡯࡫ࡷࡳࡷ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡳ࡯࡯࡫ࡷࡳࡷ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢች")
        global _1l1llll1lll_opy_
        platform_index = os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩቾ")]
        bstack1ll111l1111_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111llll_opy_ + str(platform_index)), bstack1ll11ll1ll1_opy_)
        if not os.path.exists(bstack1ll111l1111_opy_) or not os.path.isdir(bstack1ll111l1111_opy_):
            return
        logs = hook.get(bstack1l1_opy_ (u"ࠥࡰࡴ࡭ࡳࠣቿ"), [])
        with os.scandir(bstack1ll111l1111_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1l1llll1lll_opy_:
                    self.logger.info(bstack1l1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤኀ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l1_opy_ (u"ࠧࠨኁ")
                    log_entry = bstack1ll111ll111_opy_(
                        kind=bstack1l1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣኂ"),
                        message=bstack1l1_opy_ (u"ࠢࠣኃ"),
                        level=bstack1l1_opy_ (u"ࠣࠤኄ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll1l1lll11_opy_=entry.stat().st_size,
                        bstack1ll1l11111l_opy_=bstack1l1_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤኅ"),
                        bstack11l111l_opy_=os.path.abspath(entry.path),
                        bstack1ll1111lll1_opy_=hook.get(TestFramework.bstack1ll1l111l11_opy_)
                    )
                    logs.append(log_entry)
                    _1l1llll1lll_opy_.add(abs_path)
        platform_index = os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪኆ")]
        bstack1ll1l1l1111_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111llll_opy_ + str(platform_index)), bstack1ll11ll1ll1_opy_, bstack1l1llll111l_opy_)
        if not os.path.exists(bstack1ll1l1l1111_opy_) or not os.path.isdir(bstack1ll1l1l1111_opy_):
            self.logger.info(bstack1l1_opy_ (u"ࠦࡓࡵࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡧࡱࡸࡲࡩࠦࡡࡵ࠼ࠣࡿࢂࠨኇ").format(bstack1ll1l1l1111_opy_))
        else:
            self.logger.info(bstack1l1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡦࡳࡱࡰࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦኈ").format(bstack1ll1l1l1111_opy_))
            with os.scandir(bstack1ll1l1l1111_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1l1llll1lll_opy_:
                        self.logger.info(bstack1l1_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦ኉").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l1_opy_ (u"ࠢࠣኊ")
                        log_entry = bstack1ll111ll111_opy_(
                            kind=bstack1l1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥኋ"),
                            message=bstack1l1_opy_ (u"ࠤࠥኌ"),
                            level=bstack1l1_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢኍ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll1l1lll11_opy_=entry.stat().st_size,
                            bstack1ll1l11111l_opy_=bstack1l1_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦ኎"),
                            bstack11l111l_opy_=os.path.abspath(entry.path),
                            bstack1ll11l1111l_opy_=hook.get(TestFramework.bstack1ll1l111l11_opy_)
                        )
                        logs.append(log_entry)
                        _1l1llll1lll_opy_.add(abs_path)
        hook[bstack1l1_opy_ (u"ࠧࡲ࡯ࡨࡵࠥ኏")] = logs
    def bstack1ll1111ll1l_opy_(
        self,
        bstack1ll111lllll_opy_: bstack1lll1l11111_opy_,
        entries: List[bstack1ll111ll111_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡓࡆࡕࡖࡍࡔࡔ࡟ࡊࡆࠥነ"))
        req.platform_index = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lllll1l11l_opy_)
        req.execution_context.hash = str(bstack1ll111lllll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111lllll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111lllll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lll1l1111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lll1ll1l11_opy_)
            log_entry.uuid = entry.bstack1ll1111lll1_opy_ if entry.bstack1ll1111lll1_opy_ else TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1llll111ll1_opy_)
            log_entry.test_framework_state = bstack1ll111lllll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨኑ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥኒ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1lll11_opy_
                log_entry.file_path = entry.bstack11l111l_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1ll111l_opy_ = datetime.now()
            try:
                self.bstack1llll1l11ll_opy_.LogCreatedEvent(req)
                bstack1ll111lllll_opy_.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨና"), datetime.now() - bstack1l1ll111l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡻࡾࠤኔ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1ll1_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def __1ll11ll11ll_opy_(self, instance) -> None:
        bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡎࡲࡥࡩࡹࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡤࡪࡥࡷࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡩࡵࡴࡶࡲࡱࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡪࡷࡵ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡧ࡮ࡥࠢࡸࡴࡩࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡶࡸࡦࡺࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤን")
        bstack1ll111l111l_opy_ = {bstack1l1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢኖ"): bstack1ll11llllll_opy_.bstack1l1llll1l11_opy_()}
        TestFramework.bstack1ll1l11llll_opy_(instance, bstack1ll111l111l_opy_)
    @staticmethod
    def __1ll111l1l1l_opy_(instance, args):
        request, bstack1l1lllll111_opy_ = args
        bstack1ll1l1ll111_opy_ = id(bstack1l1lllll111_opy_)
        bstack1ll11l1l1l1_opy_ = instance.data[TestFramework.bstack1ll11l11l11_opy_]
        step = next(filter(lambda st: st[bstack1l1_opy_ (u"࠭ࡩࡥࠩኗ")] == bstack1ll1l1ll111_opy_, bstack1ll11l1l1l1_opy_[bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኘ")]), None)
        step.update({
            bstack1l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬኙ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11l1l1l1_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኚ")]) if st[bstack1l1_opy_ (u"ࠪ࡭ࡩ࠭ኛ")] == step[bstack1l1_opy_ (u"ࠫ࡮ࡪࠧኜ")]), None)
        if index is not None:
            bstack1ll11l1l1l1_opy_[bstack1l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኝ")][index] = step
        instance.data[TestFramework.bstack1ll11l11l11_opy_] = bstack1ll11l1l1l1_opy_
    @staticmethod
    def __1l1lllll1ll_opy_(instance, args):
        bstack1l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡭࡫࡮ࠡ࡮ࡨࡲࠥࡧࡲࡨࡵࠣ࡭ࡸࠦ࠲࠭ࠢ࡬ࡸࠥࡹࡩࡨࡰ࡬ࡪ࡮࡫ࡳࠡࡶ࡫ࡩࡷ࡫ࠠࡪࡵࠣࡲࡴࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠰ࠤࡠࡸࡥࡲࡷࡨࡷࡹ࠲ࠠࡴࡶࡨࡴࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࡥࡷ࡭ࡳࠡࡣࡵࡩࠥ࠹ࠠࡵࡪࡨࡲࠥࡺࡨࡦࠢ࡯ࡥࡸࡺࠠࡷࡣ࡯ࡹࡪࠦࡩࡴࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤኞ")
        bstack1ll11lll111_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l1lllll111_opy_ = args[1]
        bstack1ll1l1ll111_opy_ = id(bstack1l1lllll111_opy_)
        bstack1ll11l1l1l1_opy_ = instance.data[TestFramework.bstack1ll11l11l11_opy_]
        step = None
        if bstack1ll1l1ll111_opy_ is not None and bstack1ll11l1l1l1_opy_.get(bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኟ")):
            step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠨ࡫ࡧࠫአ")] == bstack1ll1l1ll111_opy_, bstack1ll11l1l1l1_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኡ")]), None)
            step.update({
                bstack1l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨኢ"): bstack1ll11lll111_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫኣ"): bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬኤ"),
                bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧእ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧኦ"): bstack1l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨኧ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11l1l1l1_opy_[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨከ")]) if st[bstack1l1_opy_ (u"ࠪ࡭ࡩ࠭ኩ")] == step[bstack1l1_opy_ (u"ࠫ࡮ࡪࠧኪ")]), None)
        if index is not None:
            bstack1ll11l1l1l1_opy_[bstack1l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫካ")][index] = step
        instance.data[TestFramework.bstack1ll11l11l11_opy_] = bstack1ll11l1l1l1_opy_
    @staticmethod
    def __1ll11l11lll_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l1_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨኬ")):
                examples = list(node.callspec.params[bstack1l1_opy_ (u"ࠧࡠࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤ࡫ࡸࡢ࡯ࡳࡰࡪ࠭ክ")].values())
            return examples
        except:
            return []
    def bstack1l1lll1lll1_opy_(self, instance: bstack1lll1l11111_opy_, bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_]):
        bstack1ll11ll111l_opy_ = (
            PytestBDDFramework.bstack1ll1l111ll1_opy_
            if bstack1lllll1l1l1_opy_[1] == bstack1lll11llll1_opy_.PRE
            else PytestBDDFramework.bstack1ll1l1l1ll1_opy_
        )
        hook = PytestBDDFramework.bstack1ll111lll11_opy_(instance, bstack1ll11ll111l_opy_)
        entries = hook.get(TestFramework.bstack1ll1111l1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1l1lll1llll_opy_, []))
        return entries
    def bstack1ll1l1l1l11_opy_(self, instance: bstack1lll1l11111_opy_, bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_]):
        bstack1ll11ll111l_opy_ = (
            PytestBDDFramework.bstack1ll1l111ll1_opy_
            if bstack1lllll1l1l1_opy_[1] == bstack1lll11llll1_opy_.PRE
            else PytestBDDFramework.bstack1ll1l1l1ll1_opy_
        )
        PytestBDDFramework.bstack1ll1l111lll_opy_(instance, bstack1ll11ll111l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1l1lll1llll_opy_, []).clear()
    @staticmethod
    def bstack1ll111lll11_opy_(instance: bstack1lll1l11111_opy_, bstack1ll11ll111l_opy_: str):
        bstack1ll1l1ll1l1_opy_ = (
            PytestBDDFramework.bstack1ll1l111l1l_opy_
            if bstack1ll11ll111l_opy_ == PytestBDDFramework.bstack1ll1l1l1ll1_opy_
            else PytestBDDFramework.bstack1ll11l111ll_opy_
        )
        bstack1ll1111l11l_opy_ = TestFramework.get_state(instance, bstack1ll11ll111l_opy_, None)
        bstack1ll1111111l_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll1l1_opy_, None) if bstack1ll1111l11l_opy_ else None
        return (
            bstack1ll1111111l_opy_[bstack1ll1111l11l_opy_][-1]
            if isinstance(bstack1ll1111111l_opy_, dict) and len(bstack1ll1111111l_opy_.get(bstack1ll1111l11l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l111lll_opy_(instance: bstack1lll1l11111_opy_, bstack1ll11ll111l_opy_: str):
        hook = PytestBDDFramework.bstack1ll111lll11_opy_(instance, bstack1ll11ll111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1111l1ll_opy_, []).clear()
    @staticmethod
    def __1ll1l111111_opy_(instance: bstack1lll1l11111_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡤࡱࡵࡨࡸࠨኮ"), None)):
            return
        if os.getenv(bstack1l1_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡎࡒࡋࡘࠨኯ"), bstack1l1_opy_ (u"ࠥ࠵ࠧኰ")) != bstack1l1_opy_ (u"ࠦ࠶ࠨ኱"):
            PytestBDDFramework.logger.warning(bstack1l1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵ࡭ࡳ࡭ࠠࡤࡣࡳࡰࡴ࡭ࠢኲ"))
            return
        bstack1ll111l1ll1_opy_ = {
            bstack1l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧኳ"): (PytestBDDFramework.bstack1ll1l111ll1_opy_, PytestBDDFramework.bstack1ll11l111ll_opy_),
            bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤኴ"): (PytestBDDFramework.bstack1ll1l1l1ll1_opy_, PytestBDDFramework.bstack1ll1l111l1l_opy_),
        }
        for when in (bstack1l1_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢኵ"), bstack1l1_opy_ (u"ࠤࡦࡥࡱࡲࠢ኶"), bstack1l1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ኷")):
            bstack1ll11l11111_opy_ = args[1].get_records(when)
            if not bstack1ll11l11111_opy_:
                continue
            records = [
                bstack1ll111ll111_opy_(
                    kind=TestFramework.bstack1ll11111111_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠢኸ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࠨኹ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11l11111_opy_
                if isinstance(getattr(r, bstack1l1_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢኺ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l1llll_opy_, bstack1ll1l1ll1l1_opy_ = bstack1ll111l1ll1_opy_.get(when, (None, None))
            bstack1ll11111lll_opy_ = TestFramework.get_state(instance, bstack1ll11l1llll_opy_, None) if bstack1ll11l1llll_opy_ else None
            bstack1ll1111111l_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll1l1_opy_, None) if bstack1ll11111lll_opy_ else None
            if isinstance(bstack1ll1111111l_opy_, dict) and len(bstack1ll1111111l_opy_.get(bstack1ll11111lll_opy_, [])) > 0:
                hook = bstack1ll1111111l_opy_[bstack1ll11111lll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1111l1ll_opy_ in hook:
                    hook[TestFramework.bstack1ll1111l1ll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1l1lll1llll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11llll1l_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll111l11ll_opy_(request.node, scenario)
        bstack1l1llll11ll_opy_ = feature.filename
        if not test_id or not test_name or not bstack1l1llll11ll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll111ll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1111l1_opy_: test_id,
            TestFramework.bstack1ll111ll1ll_opy_: test_name,
            TestFramework.bstack1ll1l11ll11_opy_: test_id,
            TestFramework.bstack1l1llll1l1l_opy_: bstack1l1llll11ll_opy_,
            TestFramework.bstack1ll11lll1l1_opy_: PytestBDDFramework.__1ll11ll11l1_opy_(feature, scenario),
            TestFramework.bstack1l1llll1ll1_opy_: code,
            TestFramework.bstack1lll1ll11ll_opy_: TestFramework.bstack1ll11l1ll11_opy_,
            TestFramework.bstack1lll1111l1l_opy_: test_name
        }
    @staticmethod
    def __1ll111l11ll_opy_(node, scenario):
        if hasattr(node, bstack1l1_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩኻ")):
            parts = node.nodeid.rsplit(bstack1l1_opy_ (u"ࠣ࡝ࠥኼ"))
            params = parts[-1]
            return bstack1l1_opy_ (u"ࠤࡾࢁࠥࡡࡻࡾࠤኽ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11ll11l1_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1l1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨኾ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1l1_opy_ (u"ࠫࡹࡧࡧࡴࠩ኿")) else [])
    @staticmethod
    def __1ll1l11l11l_opy_(location):
        return bstack1l1_opy_ (u"ࠧࡀ࠺ࠣዀ").join(filter(lambda x: isinstance(x, str), location))