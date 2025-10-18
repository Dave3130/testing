# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1ll1ll11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l11l1l_opy_ import bstack1ll1l111111_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll1lll_opy_,
    bstack1lll1l1ll1l_opy_,
    bstack1lll11lll1l_opy_,
    bstack1ll1111ll1l_opy_,
    bstack1ll11ll1l1l_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l1ll111_opy_
from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll111l1l1l_opy_ import bstack1ll11111l1l_opy_
from bstack_utils.bstack11lll1ll_opy_ import bstack1lll1lll_opy_
bstack1ll1l1l1l1l_opy_ = bstack1ll1l1ll111_opy_()
bstack1ll11lll11l_opy_ = 1.0
bstack1ll111ll111_opy_ = bstack11l111_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᖌ")
bstack11llll11l11_opy_ = bstack11l111_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᖍ")
bstack11llll111ll_opy_ = bstack11l111_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᖎ")
bstack11llll1111l_opy_ = bstack11l111_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨᖏ")
bstack11llll11111_opy_ = bstack11l111_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥᖐ")
_1ll1l1l1l11_opy_ = set()
class bstack1l11lll11ll_opy_(TestFramework):
    bstack1ll111lllll_opy_ = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᖑ")
    bstack1l1lllllll1_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࠦᖒ")
    bstack1ll11ll1lll_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᖓ")
    bstack1ll111l1ll1_opy_ = bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࠥᖔ")
    bstack1ll111l111l_opy_ = bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᖕ")
    bstack1ll1l11llll_opy_: bool
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_  = None
    bstack1llllll1l11_opy_ = None
    bstack1l1lll1lll1_opy_ = [
        bstack1lll1ll1lll_opy_.BEFORE_ALL,
        bstack1lll1ll1lll_opy_.AFTER_ALL,
        bstack1lll1ll1lll_opy_.BEFORE_EACH,
        bstack1lll1ll1lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111ll1l1_opy_: Dict[str, str],
        bstack1ll111111ll_opy_: List[str]=[bstack11l111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᖖ")],
        bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_=None,
        bstack1llllll1l11_opy_=None
    ):
        super().__init__(bstack1ll111111ll_opy_, bstack1ll111ll1l1_opy_, bstack1lll11l1l1l_opy_)
        self.bstack1ll1l11llll_opy_ = any(bstack11l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᖗ") in item.lower() for item in bstack1ll111111ll_opy_)
        self.bstack1llllll1l11_opy_ = bstack1llllll1l11_opy_
    def track_event(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll1lll_opy_.TEST or test_framework_state in bstack1l11lll11ll_opy_.bstack1l1lll1lll1_opy_:
            bstack1ll1l111111_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll1lll_opy_.NONE:
            self.logger.warning(bstack11l111_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࠨᖘ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠨࠢᖙ"))
            return
        if not self.bstack1ll1l11llll_opy_:
            self.logger.warning(bstack11l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠽ࠣᖚ") + str(str(self.bstack1ll111111ll_opy_)) + bstack11l111_opy_ (u"ࠣࠤᖛ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᖜ") + str(kwargs) + bstack11l111_opy_ (u"ࠥࠦᖝ"))
            return
        instance = self.__1l1llllll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡦࡸࡧࡴ࠿ࠥᖞ") + str(args) + bstack11l111_opy_ (u"ࠧࠨᖟ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11lll11ll_opy_.bstack1l1lll1lll1_opy_ and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack1l1ll1111_opy_.value)
                name = str(EVENTS.bstack1l1ll1111_opy_.name)+bstack11l111_opy_ (u"ࠨ࠺ࠣᖠ")+str(test_framework_state.name)
                TestFramework.bstack1ll11111lll_opy_(instance, name, bstack1ll1l1l11l1_opy_)
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴࠣࡴࡷ࡫࠺ࠡࡽࢀࠦᖡ").format(e))
        try:
            if not TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_) and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                test = bstack1l11lll11ll_opy_.__1ll111ll11l_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11l111_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖢ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠤࠥᖣ"))
            if test_framework_state == bstack1lll1ll1lll_opy_.TEST:
                if test_hook_state == bstack1lll11lll1l_opy_.PRE and not TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1ll1l111lll_opy_):
                    TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll1l111lll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l111_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖤ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠦࠧᖥ"))
                elif test_hook_state == bstack1lll11lll1l_opy_.POST and not TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1ll11ll111l_opy_):
                    TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll11ll111l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l111_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖦ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠨࠢᖧ"))
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG and test_hook_state == bstack1lll11lll1l_opy_.POST:
                bstack1l11lll11ll_opy_.__1ll1111111l_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG_REPORT and test_hook_state == bstack1lll11lll1l_opy_.POST:
                self.__1l1llll1l1l_opy_(instance, *args)
                self.__1ll1111l1l1_opy_(instance)
            elif test_framework_state in bstack1l11lll11ll_opy_.bstack1l1lll1lll1_opy_:
                self.__1ll1111l1ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᖨ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠣࠤᖩ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l1111l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11lll11ll_opy_.bstack1l1lll1lll1_opy_ and test_hook_state == bstack1lll11lll1l_opy_.POST:
                name = str(EVENTS.bstack1l1ll1111_opy_.name)+bstack11l111_opy_ (u"ࠤ࠽ࠦᖪ")+str(test_framework_state.name)
                bstack1ll1l1l11l1_opy_ = TestFramework.bstack1ll1l111l11_opy_(instance, name)
                bstack1llll11ll11_opy_.end(EVENTS.bstack1l1ll1111_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᖫ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᖬ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᖭ").format(e))
    def bstack1ll1l11ll11_opy_(self):
        return self.bstack1ll1l11llll_opy_
    def __1ll1l1l1ll1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l111_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᖮ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11llll1l_opy_(rep, [bstack11l111_opy_ (u"ࠢࡸࡪࡨࡲࠧᖯ"), bstack11l111_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᖰ"), bstack11l111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤᖱ"), bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᖲ"), bstack11l111_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧᖳ"), bstack11l111_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦᖴ")])
        return None
    def __1l1llll1l1l_opy_(self, instance: bstack1lll1l1ll1l_opy_, *args):
        result = self.__1ll1l1l1ll1_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111lll_opy_ = None
        if result.get(bstack11l111_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᖵ"), None) == bstack11l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᖶ") and len(args) > 1 and getattr(args[1], bstack11l111_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤᖷ"), None) is not None:
            failure = [{bstack11l111_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᖸ"): [args[1].excinfo.exconly(), result.get(bstack11l111_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤᖹ"), None)]}]
            bstack1111111lll_opy_ = bstack11l111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧᖺ") if bstack11l111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᖻ") in getattr(args[1].excinfo, bstack11l111_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣᖼ"), bstack11l111_opy_ (u"ࠢࠣᖽ")) else bstack11l111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᖾ")
        bstack1ll11llll11_opy_ = result.get(bstack11l111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖿ"), TestFramework.bstack1ll1l11lll1_opy_)
        if bstack1ll11llll11_opy_ != TestFramework.bstack1ll1l11lll1_opy_:
            TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11l11l11_opy_(instance, {
            TestFramework.bstack1lll1ll1ll1_opy_: failure,
            TestFramework.bstack1ll11l11111_opy_: bstack1111111lll_opy_,
            TestFramework.bstack1llll1111l1_opy_: bstack1ll11llll11_opy_,
        })
    def __1l1llllll1l_opy_(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll1lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11l1ll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l11l1ll_opy_ bstack1l1llll1111_opy_ this to be bstack11l111_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᗀ")
            if test_framework_state == bstack1lll1ll1lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11l1llll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l111_opy_ (u"ࠦࡳࡵࡤࡦࠤᗁ"), None), bstack11l111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᗂ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l111_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᗃ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111lll1l_opy_(target) if target else None
        return instance
    def __1ll1111l1ll_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1111l11l_opy_ = TestFramework.get_state(instance, bstack1l11lll11ll_opy_.bstack1l1lllllll1_opy_, {})
        if not key in bstack1ll1111l11l_opy_:
            bstack1ll1111l11l_opy_[key] = []
        bstack1ll11lll1l1_opy_ = TestFramework.get_state(instance, bstack1l11lll11ll_opy_.bstack1ll11ll1lll_opy_, {})
        if not key in bstack1ll11lll1l1_opy_:
            bstack1ll11lll1l1_opy_[key] = []
        bstack1ll11111ll1_opy_ = {
            bstack1l11lll11ll_opy_.bstack1l1lllllll1_opy_: bstack1ll1111l11l_opy_,
            bstack1l11lll11ll_opy_.bstack1ll11ll1lll_opy_: bstack1ll11lll1l1_opy_,
        }
        if test_hook_state == bstack1lll11lll1l_opy_.PRE:
            hook = {
                bstack11l111_opy_ (u"ࠢ࡬ࡧࡼࠦᗄ"): key,
                TestFramework.bstack1ll11l11l1l_opy_: uuid4().__str__(),
                TestFramework.bstack1ll111l1111_opy_: TestFramework.bstack1ll111lll11_opy_,
                TestFramework.bstack1l1lllll1ll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l111l1_opy_: [],
                TestFramework.bstack1ll11llllll_opy_: args[1] if len(args) > 1 else bstack11l111_opy_ (u"ࠨࠩᗅ"),
                TestFramework.bstack1ll11lllll1_opy_: bstack1ll11111l1l_opy_.bstack1l1lll1llll_opy_()
            }
            bstack1ll1111l11l_opy_[key].append(hook)
            bstack1ll11111ll1_opy_[bstack1l11lll11ll_opy_.bstack1ll111l1ll1_opy_] = key
        elif test_hook_state == bstack1lll11lll1l_opy_.POST:
            bstack1ll11111111_opy_ = bstack1ll1111l11l_opy_.get(key, [])
            hook = bstack1ll11111111_opy_.pop() if bstack1ll11111111_opy_ else None
            if hook:
                result = self.__1ll1l1l1ll1_opy_(*args)
                if result:
                    bstack1l1lll1ll11_opy_ = result.get(bstack11l111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᗆ"), TestFramework.bstack1ll111lll11_opy_)
                    if bstack1l1lll1ll11_opy_ != TestFramework.bstack1ll111lll11_opy_:
                        hook[TestFramework.bstack1ll111l1111_opy_] = bstack1l1lll1ll11_opy_
                hook[TestFramework.bstack1ll11l1lll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11lllll1_opy_]= bstack1ll11111l1l_opy_.bstack1l1lll1llll_opy_()
                self.bstack1l1llll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1l1lllll11l_opy_, [])
                if logs: self.bstack1l1llll11ll_opy_(instance, logs)
                bstack1ll11lll1l1_opy_[key].append(hook)
                bstack1ll11111ll1_opy_[bstack1l11lll11ll_opy_.bstack1ll111l111l_opy_] = key
        TestFramework.bstack1ll11l11l11_opy_(instance, bstack1ll11111ll1_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤᗇ") + str(bstack1ll11lll1l1_opy_) + bstack11l111_opy_ (u"ࠦࠧᗈ"))
    def __1ll11l1ll1l_opy_(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11llll1l_opy_(args[0], [bstack11l111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗉ"), bstack11l111_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢᗊ"), bstack11l111_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᗋ"), bstack11l111_opy_ (u"ࠣ࡫ࡧࡷࠧᗌ"), bstack11l111_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦᗍ"), bstack11l111_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᗎ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11l111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᗏ")) else fixturedef.get(bstack11l111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗐ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l111_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᗑ")) else None
        node = request.node if hasattr(request, bstack11l111_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᗒ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᗓ")) else None
        baseid = fixturedef.get(bstack11l111_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤᗔ"), None) or bstack11l111_opy_ (u"ࠥࠦᗕ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l111_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤᗖ")):
            target = bstack1l11lll11ll_opy_.__1ll11ll1111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l111_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᗗ")) else None
            if target and not TestFramework.bstack1ll111lll1l_opy_(target):
                self.__1ll11l1llll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᗘ") + str(test_hook_state) + bstack11l111_opy_ (u"ࠢࠣᗙ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᗚ") + str(target) + bstack11l111_opy_ (u"ࠤࠥᗛ"))
            return None
        instance = TestFramework.bstack1ll111lll1l_opy_(target)
        if not instance:
            self.logger.warning(bstack11l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧᗜ") + str(target) + bstack11l111_opy_ (u"ࠦࠧᗝ"))
            return None
        bstack1ll1111l111_opy_ = TestFramework.get_state(instance, bstack1l11lll11ll_opy_.bstack1ll111lllll_opy_, {})
        if os.getenv(bstack11l111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨᗞ"), bstack11l111_opy_ (u"ࠨ࠱ࠣᗟ")) == bstack11l111_opy_ (u"ࠢ࠲ࠤᗠ"):
            bstack1ll11ll11l1_opy_ = bstack11l111_opy_ (u"ࠣ࠼ࠥᗡ").join((scope, fixturename))
            bstack1l1lll1ll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11ll11ll_opy_ = {
                bstack11l111_opy_ (u"ࠤ࡮ࡩࡾࠨᗢ"): bstack1ll11ll11l1_opy_,
                bstack11l111_opy_ (u"ࠥࡸࡦ࡭ࡳࠣᗣ"): bstack1l11lll11ll_opy_.__1ll11l1l11l_opy_(request.node),
                bstack11l111_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧᗤ"): fixturedef,
                bstack11l111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗥ"): scope,
                bstack11l111_opy_ (u"ࠨࡴࡺࡲࡨࠦᗦ"): None,
            }
            try:
                if test_hook_state == bstack1lll11lll1l_opy_.POST and callable(getattr(args[-1], bstack11l111_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᗧ"), None)):
                    bstack1ll11ll11ll_opy_[bstack11l111_opy_ (u"ࠣࡶࡼࡴࡪࠨᗨ")] = TestFramework.bstack1ll111111l1_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll11ll11ll_opy_[bstack11l111_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᗩ")] = uuid4().__str__()
                bstack1ll11ll11ll_opy_[bstack1l11lll11ll_opy_.bstack1l1lllll1ll_opy_] = bstack1l1lll1ll1l_opy_
            elif test_hook_state == bstack1lll11lll1l_opy_.POST:
                bstack1ll11ll11ll_opy_[bstack1l11lll11ll_opy_.bstack1ll11l1lll1_opy_] = bstack1l1lll1ll1l_opy_
            if bstack1ll11ll11l1_opy_ in bstack1ll1111l111_opy_:
                bstack1ll1111l111_opy_[bstack1ll11ll11l1_opy_].update(bstack1ll11ll11ll_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦᗪ") + str(bstack1ll1111l111_opy_[bstack1ll11ll11l1_opy_]) + bstack11l111_opy_ (u"ࠦࠧᗫ"))
            else:
                bstack1ll1111l111_opy_[bstack1ll11ll11l1_opy_] = bstack1ll11ll11ll_opy_
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣᗬ") + str(len(bstack1ll1111l111_opy_)) + bstack11l111_opy_ (u"ࠨࠢᗭ"))
        TestFramework.bstack1llllllll1l_opy_(instance, bstack1l11lll11ll_opy_.bstack1ll111lllll_opy_, bstack1ll1111l111_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᗮ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠣࠤᗯ"))
        return instance
    def __1ll11l1llll_opy_(
        self,
        context: bstack1ll1111ll1l_opy_,
        test_framework_state: bstack1lll1ll1lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        ob = bstack1lll1l1ll1l_opy_(ctx, self.bstack1ll111111ll_opy_, self.bstack1ll111ll1l1_opy_, test_framework_state)
        TestFramework.bstack1ll11l11l11_opy_(ob, {
            TestFramework.bstack1lll1l11l11_opy_: context.test_framework_name,
            TestFramework.bstack1lll11ll111_opy_: context.test_framework_version,
            TestFramework.bstack1ll11ll1ll1_opy_: [],
            bstack1l11lll11ll_opy_.bstack1ll111lllll_opy_: {},
            bstack1l11lll11ll_opy_.bstack1ll11ll1lll_opy_: {},
            bstack1l11lll11ll_opy_.bstack1l1lllllll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llllllll1l_opy_(ob, TestFramework.bstack1ll11l1l111_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llllllll1l_opy_(ob, TestFramework.bstack1llllllll11_opy_, context.platform_index)
        TestFramework.bstack1lll11llll1_opy_[ctx.id] = ob
        self.logger.debug(bstack11l111_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᗰ") + str(TestFramework.bstack1lll11llll1_opy_.keys()) + bstack11l111_opy_ (u"ࠥࠦᗱ"))
        return ob
    def bstack1ll1l1l11ll_opy_(self, instance: bstack1lll1l1ll1l_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll11l111ll_opy_ = (
            bstack1l11lll11ll_opy_.bstack1ll111l1ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else bstack1l11lll11ll_opy_.bstack1ll111l111l_opy_
        )
        hook = bstack1l11lll11ll_opy_.bstack1ll11l1111l_opy_(instance, bstack1ll11l111ll_opy_)
        entries = hook.get(TestFramework.bstack1ll11l111l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_, []))
        return entries
    def bstack1ll1l11111l_opy_(self, instance: bstack1lll1l1ll1l_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll11l111ll_opy_ = (
            bstack1l11lll11ll_opy_.bstack1ll111l1ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else bstack1l11lll11ll_opy_.bstack1ll111l111l_opy_
        )
        bstack1l11lll11ll_opy_.bstack1ll1l1111ll_opy_(instance, bstack1ll11l111ll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_, []).clear()
    def bstack1l1llll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡶ࡭ࡲ࡯࡬ࡢࡴࠣࡸࡴࠦࡴࡩࡧࠣࡎࡦࡼࡡࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡅ࡫ࡩࡨࡱࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡮ࡴࡳࡪࡦࡨࠤࢃ࠵࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠵ࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠯ࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡸࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨࠠࡪࡰࠣ࡭ࡹࡹࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡎ࡬ࠠࡢࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣࡸ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡱࡦࡺࡣࡩࡧࡶࠤࡦࠦ࡭ࡰࡦ࡬ࡪ࡮࡫ࡤࠡࡪࡲࡳࡰ࠳࡬ࡦࡸࡨࡰࠥ࡬ࡩ࡭ࡧ࠯ࠤ࡮ࡺࠠࡤࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࠥࡽࡩࡵࡪࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡔ࡫ࡰ࡭ࡱࡧࡲ࡭ࡻ࠯ࠤ࡮ࡺࠠࡱࡴࡲࡧࡪࡹࡳࡦࡵࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡲ࡯ࡤࡣࡷࡩࡩࠦࡩ࡯ࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡧࡿࠠࡳࡧࡳࡰࡦࡩࡩ࡯ࡩࠣࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡘ࡭࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࡶࠤࡦࡸࡥࠡࡣࡧࡨࡪࡪࠠࡵࡱࠣࡸ࡭࡫ࠠࡩࡱࡲ࡯ࠬࡹࠠࠣ࡮ࡲ࡫ࡸࠨࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬࠼ࠣࡘ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹࠠࡢࡰࡧࠤ࡭ࡵ࡯࡬ࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩ࡚ࠥࡥࡴࡶࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᗲ")
        global _1ll1l1l1l11_opy_
        platform_index = os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᗳ")]
        bstack1ll1l1l111l_opy_ = os.path.join(bstack1ll1l1l1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack11llll1111l_opy_)
        if not os.path.exists(bstack1ll1l1l111l_opy_) or not os.path.isdir(bstack1ll1l1l111l_opy_):
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶࡶࠤࡹࡵࠠࡱࡴࡲࡧࡪࡹࡳࠡࡽࢀࠦᗴ").format(bstack1ll1l1l111l_opy_))
            return
        logs = hook.get(bstack11l111_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᗵ"), [])
        with os.scandir(bstack1ll1l1l111l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l1l1l11_opy_:
                    self.logger.info(bstack11l111_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᗶ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l111_opy_ (u"ࠤࠥᗷ")
                    log_entry = bstack1ll11ll1l1l_opy_(
                        kind=bstack11l111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᗸ"),
                        message=bstack11l111_opy_ (u"ࠦࠧᗹ"),
                        level=bstack11l111_opy_ (u"ࠧࠨᗺ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1llll11l1_opy_=entry.stat().st_size,
                        bstack1ll1111lll1_opy_=bstack11l111_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᗻ"),
                        bstack11ll1ll_opy_=os.path.abspath(entry.path),
                        bstack1ll1111llll_opy_=hook.get(TestFramework.bstack1ll11l11l1l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l1l1l11_opy_.add(abs_path)
        platform_index = os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᗼ")]
        bstack1ll1l111ll1_opy_ = os.path.join(bstack1ll1l1l1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack11llll1111l_opy_, bstack11llll11111_opy_)
        if not os.path.exists(bstack1ll1l111ll1_opy_) or not os.path.isdir(bstack1ll1l111ll1_opy_):
            self.logger.info(bstack11l111_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥᗽ").format(bstack1ll1l111ll1_opy_))
        else:
            self.logger.info(bstack11l111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣᗾ").format(bstack1ll1l111ll1_opy_))
            with os.scandir(bstack1ll1l111ll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l1l1l11_opy_:
                        self.logger.info(bstack11l111_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᗿ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l111_opy_ (u"ࠦࠧᘀ")
                        log_entry = bstack1ll11ll1l1l_opy_(
                            kind=bstack11l111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᘁ"),
                            message=bstack11l111_opy_ (u"ࠨࠢᘂ"),
                            level=bstack11l111_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᘃ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1llll11l1_opy_=entry.stat().st_size,
                            bstack1ll1111lll1_opy_=bstack11l111_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᘄ"),
                            bstack11ll1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll1l1ll1l1_opy_=hook.get(TestFramework.bstack1ll11l11l1l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l1l1l11_opy_.add(abs_path)
        hook[bstack11l111_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᘅ")] = logs
    def bstack1l1llll11ll_opy_(
        self,
        bstack1ll111llll1_opy_: bstack1lll1l1ll1l_opy_,
        entries: List[bstack1ll11ll1l1l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢᘆ"))
        req.platform_index = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1llllllll11_opy_)
        req.execution_context.hash = str(bstack1ll111llll1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111llll1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111llll1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll11ll111_opy_)
            log_entry.uuid = entry.bstack1ll1111llll_opy_
            log_entry.test_framework_state = bstack1ll111llll1_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᘇ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack11l111_opy_ (u"ࠧࠨᘈ")
            if entry.kind == bstack11l111_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᘉ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llll11l1_opy_
                log_entry.file_path = entry.bstack11ll1ll_opy_
        def bstack1ll11l1l1l1_opy_():
            bstack1l1ll1ll1_opy_ = datetime.now()
            try:
                self.bstack1llllll1l11_opy_.LogCreatedEvent(req)
                bstack1ll111llll1_opy_.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᘊ"), datetime.now() - bstack1l1ll1ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࢀࢃࠢᘋ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11l1l1l1_opy_)
    def __1ll1111l1l1_opy_(self, instance) -> None:
        bstack11l111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡌࡰࡣࡧࡷࠥࡩࡵࡴࡶࡲࡱࠥࡺࡡࡨࡵࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡵࡩࡦࡺࡥࡴࠢࡤࠤࡩ࡯ࡣࡵࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡱ࡫ࡶࡦ࡮ࠣࡧࡺࡹࡴࡰ࡯ࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡨࡵࡳࡲࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡷࡶࡸࡴࡳࡔࡢࡩࡐࡥࡳࡧࡧࡦࡴࠣࡥࡳࡪࠠࡶࡲࡧࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡴࡶࡤࡸࡪࠦࡵࡴ࡫ࡱ࡫ࠥࡹࡥࡵࡡࡶࡸࡦࡺࡥࡠࡧࡱࡸࡷ࡯ࡥࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘌ")
        bstack1ll11111ll1_opy_ = {bstack11l111_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧᘍ"): bstack1ll11111l1l_opy_.bstack1l1lll1llll_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11l11l11_opy_(instance, bstack1ll11111ll1_opy_)
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1lll1l1ll1l_opy_, bstack1ll11l111ll_opy_: str):
        bstack1ll11l1ll11_opy_ = (
            bstack1l11lll11ll_opy_.bstack1ll11ll1lll_opy_
            if bstack1ll11l111ll_opy_ == bstack1l11lll11ll_opy_.bstack1ll111l111l_opy_
            else bstack1l11lll11ll_opy_.bstack1l1lllllll1_opy_
        )
        bstack1ll1l111l1l_opy_ = TestFramework.get_state(instance, bstack1ll11l111ll_opy_, None)
        bstack1l1lllll1l1_opy_ = TestFramework.get_state(instance, bstack1ll11l1ll11_opy_, None) if bstack1ll1l111l1l_opy_ else None
        return (
            bstack1l1lllll1l1_opy_[bstack1ll1l111l1l_opy_][-1]
            if isinstance(bstack1l1lllll1l1_opy_, dict) and len(bstack1l1lllll1l1_opy_.get(bstack1ll1l111l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l1111ll_opy_(instance: bstack1lll1l1ll1l_opy_, bstack1ll11l111ll_opy_: str):
        hook = bstack1l11lll11ll_opy_.bstack1ll11l1111l_opy_(instance, bstack1ll11l111ll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l111l1_opy_, []).clear()
    @staticmethod
    def __1ll1111111l_opy_(instance: bstack1lll1l1ll1l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l111_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡧࡴࡸࡤࡴࠤᘎ"), None)):
            return
        if os.getenv(bstack11l111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡑࡕࡇࡔࠤᘏ"), bstack11l111_opy_ (u"ࠨ࠱ࠣᘐ")) != bstack11l111_opy_ (u"ࠢ࠲ࠤᘑ"):
            bstack1l11lll11ll_opy_.logger.warning(bstack11l111_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡩ࡯ࡩࠣࡧࡦࡶ࡬ࡰࡩࠥᘒ"))
            return
        bstack1l1llll1lll_opy_ = {
            bstack11l111_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᘓ"): (bstack1l11lll11ll_opy_.bstack1ll111l1ll1_opy_, bstack1l11lll11ll_opy_.bstack1l1lllllll1_opy_),
            bstack11l111_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᘔ"): (bstack1l11lll11ll_opy_.bstack1ll111l111l_opy_, bstack1l11lll11ll_opy_.bstack1ll11ll1lll_opy_),
        }
        for when in (bstack11l111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᘕ"), bstack11l111_opy_ (u"ࠧࡩࡡ࡭࡮ࠥᘖ"), bstack11l111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᘗ")):
            bstack1ll111l1lll_opy_ = args[1].get_records(when)
            if not bstack1ll111l1lll_opy_:
                continue
            records = [
                bstack1ll11ll1l1l_opy_(
                    kind=TestFramework.bstack1ll1111ll11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l111_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠥᘘ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l111_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࠤᘙ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll111l1lll_opy_
                if isinstance(getattr(r, bstack11l111_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᘚ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11ll1l11_opy_, bstack1ll11l1ll11_opy_ = bstack1l1llll1lll_opy_.get(when, (None, None))
            bstack1ll11111l11_opy_ = TestFramework.get_state(instance, bstack1ll11ll1l11_opy_, None) if bstack1ll11ll1l11_opy_ else None
            bstack1l1lllll1l1_opy_ = TestFramework.get_state(instance, bstack1ll11l1ll11_opy_, None) if bstack1ll11111l11_opy_ else None
            if isinstance(bstack1l1lllll1l1_opy_, dict) and len(bstack1l1lllll1l1_opy_.get(bstack1ll11111l11_opy_, [])) > 0:
                hook = bstack1l1lllll1l1_opy_[bstack1ll11111l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l111l1_opy_ in hook:
                    hook[TestFramework.bstack1ll11l111l1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll111ll11l_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11lll11ll_opy_.__1ll11ll1111_opy_(test.location) if hasattr(test, bstack11l111_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᘛ")) else getattr(test, bstack11l111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᘜ"), None)
        test_name = test.name if hasattr(test, bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘝ")) else None
        bstack1ll111l1l11_opy_ = test.fspath.strpath if hasattr(test, bstack11l111_opy_ (u"ࠨࡦࡴࡲࡤࡸ࡭ࠨᘞ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll111l1l11_opy_:
            return None
        code = None
        if hasattr(test, bstack11l111_opy_ (u"ࠢࡰࡤ࡭ࠦᘟ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll111l1_opy_ = []
        try:
            bstack11llll111l1_opy_ = bstack1lll1lll_opy_.bstack1l1l1l11_opy_(test)
        except:
            bstack1l11lll11ll_opy_.logger.warning(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠬࠡࡶࡨࡷࡹࠦࡳࡤࡱࡳࡩࡸࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡳࡧࡶࡳࡱࡼࡥࡥࠢ࡬ࡲࠥࡉࡌࡊࠤᘠ"))
        return {
            TestFramework.bstack1lll1lll1l1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11l11l_opy_: test_id,
            TestFramework.bstack1ll1l11l111_opy_: test_name,
            TestFramework.bstack1l1llll1l11_opy_: getattr(test, bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᘡ"), None),
            TestFramework.bstack1l1llllllll_opy_: bstack1ll111l1l11_opy_,
            TestFramework.bstack1ll111l11l1_opy_: bstack1l11lll11ll_opy_.__1ll11l1l11l_opy_(test),
            TestFramework.bstack1ll11lll111_opy_: code,
            TestFramework.bstack1llll1111l1_opy_: TestFramework.bstack1ll1l11lll1_opy_,
            TestFramework.bstack1lll11l111l_opy_: test_id,
            TestFramework.bstack1l11111l11l_opy_: bstack11llll111l1_opy_
        }
    @staticmethod
    def __1ll11l1l11l_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack11l111_opy_ (u"ࠥࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠣᘢ"), [])
            markers.extend([getattr(m, bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᘣ"), None) for m in own_markers if getattr(m, bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘤ"), None)])
            current = getattr(current, bstack11l111_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᘥ"), None)
        return markers
    @staticmethod
    def __1ll11ll1111_opy_(location):
        return bstack11l111_opy_ (u"ࠢ࠻࠼ࠥᘦ").join(filter(lambda x: isinstance(x, str), location))