# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1ll1lll111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1lll1ll1_opy_ import bstack1ll11ll1lll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll11l1ll_opy_,
    bstack1lll1l1l1ll_opy_,
    bstack1lll1llll11_opy_,
    bstack1ll1l1lllll_opy_,
    bstack1ll11lll111_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l11ll11_opy_
from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l11111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll111l1l1l_opy_ import bstack1l1lllll1l1_opy_
from bstack_utils.bstack11llll1l_opy_ import bstack1l11llll_opy_
bstack1ll1111llll_opy_ = bstack1ll1l11ll11_opy_()
bstack1ll1111ll1l_opy_ = 1.0
bstack1ll1l11lll1_opy_ = bstack1ll1l_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤᕤ")
bstack11llll1ll11_opy_ = bstack1ll1l_opy_ (u"ࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨᕥ")
bstack11llll1l11l_opy_ = bstack1ll1l_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᕦ")
bstack11llll1l1l1_opy_ = bstack1ll1l_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣᕧ")
bstack11llll1l1ll_opy_ = bstack1ll1l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧᕨ")
_1ll11l11111_opy_ = set()
class bstack1l1l111ll11_opy_(TestFramework):
    bstack1ll1l1l11l1_opy_ = bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᕩ")
    bstack1ll11ll1l1l_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨᕪ")
    bstack1ll11111lll_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᕫ")
    bstack1ll111l1lll_opy_ = bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧᕬ")
    bstack1ll1l1111ll_opy_ = bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᕭ")
    bstack1ll1l1lll1l_opy_: bool
    bstack1lll11lllll_opy_: bstack1lll1l11111_opy_  = None
    bstack1llll1l1ll1_opy_ = None
    bstack1ll1111l11l_opy_ = [
        bstack1llll11l1ll_opy_.BEFORE_ALL,
        bstack1llll11l1ll_opy_.AFTER_ALL,
        bstack1llll11l1ll_opy_.BEFORE_EACH,
        bstack1llll11l1ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l1llllll11_opy_: Dict[str, str],
        bstack1ll1ll111ll_opy_: List[str]=[bstack1ll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᕮ")],
        bstack1lll11lllll_opy_: bstack1lll1l11111_opy_=None,
        bstack1llll1l1ll1_opy_=None
    ):
        super().__init__(bstack1ll1ll111ll_opy_, bstack1l1llllll11_opy_, bstack1lll11lllll_opy_)
        self.bstack1ll1l1lll1l_opy_ = any(bstack1ll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᕯ") in item.lower() for item in bstack1ll1ll111ll_opy_)
        self.bstack1llll1l1ll1_opy_ = bstack1llll1l1ll1_opy_
    def track_event(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll11l1ll_opy_.TEST or test_framework_state in bstack1l1l111ll11_opy_.bstack1ll1111l11l_opy_:
            bstack1ll11ll1lll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll11l1ll_opy_.NONE:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣᕰ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠣࠤᕱ"))
            return
        if not self.bstack1ll1l1lll1l_opy_:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥᕲ") + str(str(self.bstack1ll1ll111ll_opy_)) + bstack1ll1l_opy_ (u"ࠥࠦᕳ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᕴ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠧࠨᕵ"))
            return
        instance = self.__1ll1l111lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧᕶ") + str(args) + bstack1ll1l_opy_ (u"ࠢࠣᕷ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l111ll11_opy_.bstack1ll1111l11l_opy_ and test_hook_state == bstack1lll1llll11_opy_.PRE:
                bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack11ll11111l_opy_.value)
                name = str(EVENTS.bstack11ll11111l_opy_.name)+bstack1ll1l_opy_ (u"ࠣ࠼ࠥᕸ")+str(test_framework_state.name)
                TestFramework.bstack1ll1l1l1l11_opy_(instance, name, bstack1l1lllll111_opy_)
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶࠥࡶࡲࡦ࠼ࠣࡿࢂࠨᕹ").format(e))
        try:
            if not TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1ll11l1llll_opy_) and test_hook_state == bstack1lll1llll11_opy_.PRE:
                test = bstack1l1l111ll11_opy_.__1ll1l1l1111_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡰࡴࡧࡤࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᕺ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠦࠧᕻ"))
            if test_framework_state == bstack1llll11l1ll_opy_.TEST:
                if test_hook_state == bstack1lll1llll11_opy_.PRE and not TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1ll11l11l11_opy_):
                    TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll11l11l11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡴࡶࡤࡶࡹࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᕼ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠨࠢᕽ"))
                elif test_hook_state == bstack1lll1llll11_opy_.POST and not TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1ll11llllll_opy_):
                    TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll11llllll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡨࡲࡩࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᕾ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠣࠤᕿ"))
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG and test_hook_state == bstack1lll1llll11_opy_.POST:
                bstack1l1l111ll11_opy_.__1l1llll1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG_REPORT and test_hook_state == bstack1lll1llll11_opy_.POST:
                self.__1ll1l1111l1_opy_(instance, *args)
                self.__1ll11ll1ll1_opy_(instance)
            elif test_framework_state in bstack1l1l111ll11_opy_.bstack1ll1111l11l_opy_:
                self.__1ll11ll1l11_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᖀ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠥࠦᖁ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1llll1lll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l111ll11_opy_.bstack1ll1111l11l_opy_ and test_hook_state == bstack1lll1llll11_opy_.POST:
                name = str(EVENTS.bstack11ll11111l_opy_.name)+bstack1ll1l_opy_ (u"ࠦ࠿ࠨᖂ")+str(test_framework_state.name)
                bstack1l1lllll111_opy_ = TestFramework.bstack1l1lllll1ll_opy_(instance, name)
                bstack1llll1l1l11_opy_.end(EVENTS.bstack11ll11111l_opy_.value, bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᖃ"), bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᖄ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᖅ").format(e))
    def bstack1ll11lll1ll_opy_(self):
        return self.bstack1ll1l1lll1l_opy_
    def __1ll111l111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1ll1l_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᖆ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111lll1l_opy_(rep, [bstack1ll1l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᖇ"), bstack1ll1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖈ"), bstack1ll1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦᖉ"), bstack1ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧᖊ"), bstack1ll1l_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢᖋ"), bstack1ll1l_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨᖌ")])
        return None
    def __1ll1l1111l1_opy_(self, instance: bstack1lll1l1l1ll_opy_, *args):
        result = self.__1ll111l111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l11l1_opy_ = None
        if result.get(bstack1ll1l_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᖍ"), None) == bstack1ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᖎ") and len(args) > 1 and getattr(args[1], bstack1ll1l_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦᖏ"), None) is not None:
            failure = [{bstack1ll1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᖐ"): [args[1].excinfo.exconly(), result.get(bstack1ll1l_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦᖑ"), None)]}]
            bstack11111l11l1_opy_ = bstack1ll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᖒ") if bstack1ll1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᖓ") in getattr(args[1].excinfo, bstack1ll1l_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥᖔ"), bstack1ll1l_opy_ (u"ࠤࠥᖕ")) else bstack1ll1l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᖖ")
        bstack1ll1l11ll1l_opy_ = result.get(bstack1ll1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᖗ"), TestFramework.bstack1ll111ll1l1_opy_)
        if bstack1ll1l11ll1l_opy_ != TestFramework.bstack1ll111ll1l1_opy_:
            TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1l1llllll1l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l1l11ll_opy_(instance, {
            TestFramework.bstack1llll1111ll_opy_: failure,
            TestFramework.bstack1ll11llll11_opy_: bstack11111l11l1_opy_,
            TestFramework.bstack1lll1l11l1l_opy_: bstack1ll1l11ll1l_opy_,
        })
    def __1ll1l111lll_opy_(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll11l1ll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11111ll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll111ll111_opy_ bstack1ll111l1111_opy_ this to be bstack1ll1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᖘ")
            if test_framework_state == bstack1llll11l1ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1111lll1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1ll1l_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᖙ"), None), bstack1ll1l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᖚ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1ll1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᖛ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1lllllll1_opy_(target) if target else None
        return instance
    def __1ll11ll1l11_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1l111l_opy_ = TestFramework.get_state(instance, bstack1l1l111ll11_opy_.bstack1ll11ll1l1l_opy_, {})
        if not key in bstack1ll1l1l111l_opy_:
            bstack1ll1l1l111l_opy_[key] = []
        bstack1ll111lllll_opy_ = TestFramework.get_state(instance, bstack1l1l111ll11_opy_.bstack1ll11111lll_opy_, {})
        if not key in bstack1ll111lllll_opy_:
            bstack1ll111lllll_opy_[key] = []
        bstack1ll11l1ll1l_opy_ = {
            bstack1l1l111ll11_opy_.bstack1ll11ll1l1l_opy_: bstack1ll1l1l111l_opy_,
            bstack1l1l111ll11_opy_.bstack1ll11111lll_opy_: bstack1ll111lllll_opy_,
        }
        if test_hook_state == bstack1lll1llll11_opy_.PRE:
            hook = {
                bstack1ll1l_opy_ (u"ࠤ࡮ࡩࡾࠨᖜ"): key,
                TestFramework.bstack1ll1l1ll1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l111ll_opy_: TestFramework.bstack1ll1l11l1ll_opy_,
                TestFramework.bstack1ll1l111111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11ll111l_opy_: [],
                TestFramework.bstack1ll11l1l111_opy_: args[1] if len(args) > 1 else bstack1ll1l_opy_ (u"ࠪࠫᖝ"),
                TestFramework.bstack1ll11ll11l1_opy_: bstack1l1lllll1l1_opy_.bstack1ll11l1111l_opy_()
            }
            bstack1ll1l1l111l_opy_[key].append(hook)
            bstack1ll11l1ll1l_opy_[bstack1l1l111ll11_opy_.bstack1ll111l1lll_opy_] = key
        elif test_hook_state == bstack1lll1llll11_opy_.POST:
            bstack1ll11lll1l1_opy_ = bstack1ll1l1l111l_opy_.get(key, [])
            hook = bstack1ll11lll1l1_opy_.pop() if bstack1ll11lll1l1_opy_ else None
            if hook:
                result = self.__1ll111l111l_opy_(*args)
                if result:
                    bstack1ll1ll11l11_opy_ = result.get(bstack1ll1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᖞ"), TestFramework.bstack1ll1l11l1ll_opy_)
                    if bstack1ll1ll11l11_opy_ != TestFramework.bstack1ll1l11l1ll_opy_:
                        hook[TestFramework.bstack1ll11l111ll_opy_] = bstack1ll1ll11l11_opy_
                hook[TestFramework.bstack1ll11111l1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11ll11l1_opy_]= bstack1l1lllll1l1_opy_.bstack1ll11l1111l_opy_()
                self.bstack1ll11l1l1ll_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll111ll1ll_opy_, [])
                if logs: self.bstack1ll1l1ll111_opy_(instance, logs)
                bstack1ll111lllll_opy_[key].append(hook)
                bstack1ll11l1ll1l_opy_[bstack1l1l111ll11_opy_.bstack1ll1l1111ll_opy_] = key
        TestFramework.bstack1ll1l1l11ll_opy_(instance, bstack1ll11l1ll1l_opy_)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦᖟ") + str(bstack1ll111lllll_opy_) + bstack1ll1l_opy_ (u"ࠨࠢᖠ"))
    def __1ll11111ll1_opy_(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111lll1l_opy_(args[0], [bstack1ll1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᖡ"), bstack1ll1l_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤᖢ"), bstack1ll1l_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᖣ"), bstack1ll1l_opy_ (u"ࠥ࡭ࡩࡹࠢᖤ"), bstack1ll1l_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨᖥ"), bstack1ll1l_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧᖦ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1ll1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᖧ")) else fixturedef.get(bstack1ll1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᖨ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1ll1l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨᖩ")) else None
        node = request.node if hasattr(request, bstack1ll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᖪ")) else None
        target = request.node.nodeid if hasattr(node, bstack1ll1l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᖫ")) else None
        baseid = fixturedef.get(bstack1ll1l_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦᖬ"), None) or bstack1ll1l_opy_ (u"ࠧࠨᖭ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1ll1l_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦᖮ")):
            target = bstack1l1l111ll11_opy_.__1ll1l1l1l1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1ll1l_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤᖯ")) else None
            if target and not TestFramework.bstack1l1lllllll1_opy_(target):
                self.__1ll1111lll1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᖰ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠤࠥᖱ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣᖲ") + str(target) + bstack1ll1l_opy_ (u"ࠦࠧᖳ"))
            return None
        instance = TestFramework.bstack1l1lllllll1_opy_(target)
        if not instance:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢᖴ") + str(target) + bstack1ll1l_opy_ (u"ࠨࠢᖵ"))
            return None
        bstack1ll11111111_opy_ = TestFramework.get_state(instance, bstack1l1l111ll11_opy_.bstack1ll1l1l11l1_opy_, {})
        if os.getenv(bstack1ll1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣᖶ"), bstack1ll1l_opy_ (u"ࠣ࠳ࠥᖷ")) == bstack1ll1l_opy_ (u"ࠤ࠴ࠦᖸ"):
            bstack1ll1l1l1ll1_opy_ = bstack1ll1l_opy_ (u"ࠥ࠾ࠧᖹ").join((scope, fixturename))
            bstack1ll1111l1l1_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11l11ll1_opy_ = {
                bstack1ll1l_opy_ (u"ࠦࡰ࡫ࡹࠣᖺ"): bstack1ll1l1l1ll1_opy_,
                bstack1ll1l_opy_ (u"ࠧࡺࡡࡨࡵࠥᖻ"): bstack1l1l111ll11_opy_.__1ll111l1ll1_opy_(request.node),
                bstack1ll1l_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢᖼ"): fixturedef,
                bstack1ll1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᖽ"): scope,
                bstack1ll1l_opy_ (u"ࠣࡶࡼࡴࡪࠨᖾ"): None,
            }
            try:
                if test_hook_state == bstack1lll1llll11_opy_.POST and callable(getattr(args[-1], bstack1ll1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨᖿ"), None)):
                    bstack1ll11l11ll1_opy_[bstack1ll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣᗀ")] = TestFramework.bstack1ll11l1ll11_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1llll11_opy_.PRE:
                bstack1ll11l11ll1_opy_[bstack1ll1l_opy_ (u"ࠦࡺࡻࡩࡥࠤᗁ")] = uuid4().__str__()
                bstack1ll11l11ll1_opy_[bstack1l1l111ll11_opy_.bstack1ll1l111111_opy_] = bstack1ll1111l1l1_opy_
            elif test_hook_state == bstack1lll1llll11_opy_.POST:
                bstack1ll11l11ll1_opy_[bstack1l1l111ll11_opy_.bstack1ll11111l1l_opy_] = bstack1ll1111l1l1_opy_
            if bstack1ll1l1l1ll1_opy_ in bstack1ll11111111_opy_:
                bstack1ll11111111_opy_[bstack1ll1l1l1ll1_opy_].update(bstack1ll11l11ll1_opy_)
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨᗂ") + str(bstack1ll11111111_opy_[bstack1ll1l1l1ll1_opy_]) + bstack1ll1l_opy_ (u"ࠨࠢᗃ"))
            else:
                bstack1ll11111111_opy_[bstack1ll1l1l1ll1_opy_] = bstack1ll11l11ll1_opy_
                self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥᗄ") + str(len(bstack1ll11111111_opy_)) + bstack1ll1l_opy_ (u"ࠣࠤᗅ"))
        TestFramework.bstack1111111ll1_opy_(instance, bstack1l1l111ll11_opy_.bstack1ll1l1l11l1_opy_, bstack1ll11111111_opy_)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᗆ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠥࠦᗇ"))
        return instance
    def __1ll1111lll1_opy_(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll111l_opy_.create_context(target)
        ob = bstack1lll1l1l1ll_opy_(ctx, self.bstack1ll1ll111ll_opy_, self.bstack1l1llllll11_opy_, test_framework_state)
        TestFramework.bstack1ll1l1l11ll_opy_(ob, {
            TestFramework.bstack1llll11llll_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l11l11_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l11l111_opy_: [],
            bstack1l1l111ll11_opy_.bstack1ll1l1l11l1_opy_: {},
            bstack1l1l111ll11_opy_.bstack1ll11111lll_opy_: {},
            bstack1l1l111ll11_opy_.bstack1ll11ll1l1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111111ll1_opy_(ob, TestFramework.bstack1ll11111l11_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111111ll1_opy_(ob, TestFramework.bstack1lllllllll1_opy_, context.platform_index)
        TestFramework.bstack1lll1ll11ll_opy_[ctx.id] = ob
        self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦᗈ") + str(TestFramework.bstack1lll1ll11ll_opy_.keys()) + bstack1ll1l_opy_ (u"ࠧࠨᗉ"))
        return ob
    def bstack1ll1l111l1l_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_]):
        bstack1ll111lll11_opy_ = (
            bstack1l1l111ll11_opy_.bstack1ll111l1lll_opy_
            if bstack1llllll111l_opy_[1] == bstack1lll1llll11_opy_.PRE
            else bstack1l1l111ll11_opy_.bstack1ll1l1111ll_opy_
        )
        hook = bstack1l1l111ll11_opy_.bstack1ll111ll11l_opy_(instance, bstack1ll111lll11_opy_)
        entries = hook.get(TestFramework.bstack1ll11ll111l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, []))
        return entries
    def bstack1ll11l1lll1_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_]):
        bstack1ll111lll11_opy_ = (
            bstack1l1l111ll11_opy_.bstack1ll111l1lll_opy_
            if bstack1llllll111l_opy_[1] == bstack1lll1llll11_opy_.PRE
            else bstack1l1l111ll11_opy_.bstack1ll1l1111ll_opy_
        )
        bstack1l1l111ll11_opy_.bstack1ll1111l111_opy_(instance, bstack1ll111lll11_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, []).clear()
    def bstack1ll11l1l1ll_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡷࡵࡣࡦࡵࡶࡩࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡸ࡯࡭ࡪ࡮ࡤࡶࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡡࡷࡣࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩ࡫ࡶࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡇ࡭࡫ࡣ࡬ࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡩ࡯ࡵ࡬ࡨࡪࠦࡾ࠰࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠰ࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡆࡰࡴࠣࡩࡦࡩࡨࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠱ࠦࡲࡦࡲ࡯ࡥࡨ࡫ࡳࠡࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧࠦࡷࡪࡶ࡫ࠤࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣࠢ࡬ࡲࠥ࡯ࡴࡴࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡉࡧࠢࡤࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡺࡨࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡳࡡࡵࡥ࡫ࡩࡸࠦࡡࠡ࡯ࡲࡨ࡮࡬ࡩࡦࡦࠣ࡬ࡴࡵ࡫࠮࡮ࡨࡺࡪࡲࠠࡧ࡫࡯ࡩ࠱ࠦࡩࡵࠢࡦࡶࡪࡧࡴࡦࡵࠣࡥࠥࡒ࡯ࡨࡇࡱࡸࡷࡿࠠࡰࡤ࡭ࡩࡨࡺࠠࡸ࡫ࡷ࡬ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡧࡩࡹࡧࡩ࡭ࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡖ࡭ࡲ࡯࡬ࡢࡴ࡯ࡽ࠱ࠦࡩࡵࠢࡳࡶࡴࡩࡥࡴࡵࡨࡷࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠ࡭ࡱࡦࡥࡹ࡫ࡤࠡ࡫ࡱࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡢࡺࠢࡵࡩࡵࡲࡡࡤ࡫ࡱ࡫ࠥࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡚ࠥࡨࡦࠢࡦࡶࡪࡧࡴࡦࡦࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡡࡳࡧࠣࡥࡩࡪࡥࡥࠢࡷࡳࠥࡺࡨࡦࠢ࡫ࡳࡴࡱࠧࡴࠢࠥࡰࡴ࡭ࡳࠣࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮࠾࡚ࠥࡨࡦࠢࡨࡺࡪࡴࡴࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡱࡵࡧࡴࠢࡤࡲࡩࠦࡨࡰࡱ࡮ࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠣࡱࡴࡴࡩࡵࡱࡵ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡱࡴࡴࡩࡵࡱࡵ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᗊ")
        global _1ll11l11111_opy_
        platform_index = os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᗋ")]
        bstack1ll1ll111l1_opy_ = os.path.join(bstack1ll1111llll_opy_, (bstack1ll1l11lll1_opy_ + str(platform_index)), bstack11llll1l1l1_opy_)
        if not os.path.exists(bstack1ll1ll111l1_opy_) or not os.path.isdir(bstack1ll1ll111l1_opy_):
            self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸࡸࠦࡴࡰࠢࡳࡶࡴࡩࡥࡴࡵࠣࡿࢂࠨᗌ").format(bstack1ll1ll111l1_opy_))
            return
        logs = hook.get(bstack1ll1l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᗍ"), [])
        with os.scandir(bstack1ll1ll111l1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l11111_opy_:
                    self.logger.info(bstack1ll1l_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᗎ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1ll1l_opy_ (u"ࠦࠧᗏ")
                    log_entry = bstack1ll11lll111_opy_(
                        kind=bstack1ll1l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᗐ"),
                        message=bstack1ll1l_opy_ (u"ࠨࠢᗑ"),
                        level=bstack1ll1l_opy_ (u"ࠢࠣᗒ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11ll11ll_opy_=entry.stat().st_size,
                        bstack1l1llllllll_opy_=bstack1ll1l_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᗓ"),
                        bstack1ll1ll_opy_=os.path.abspath(entry.path),
                        bstack1ll11l11lll_opy_=hook.get(TestFramework.bstack1ll1l1ll1ll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l11111_opy_.add(abs_path)
        platform_index = os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᗔ")]
        bstack1ll111l11l1_opy_ = os.path.join(bstack1ll1111llll_opy_, (bstack1ll1l11lll1_opy_ + str(platform_index)), bstack11llll1l1l1_opy_, bstack11llll1l1ll_opy_)
        if not os.path.exists(bstack1ll111l11l1_opy_) or not os.path.isdir(bstack1ll111l11l1_opy_):
            self.logger.info(bstack1ll1l_opy_ (u"ࠥࡒࡴࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡦࡰࡷࡱࡨࠥࡧࡴ࠻ࠢࡾࢁࠧᗕ").format(bstack1ll111l11l1_opy_))
        else:
            self.logger.info(bstack1ll1l_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᗖ").format(bstack1ll111l11l1_opy_))
            with os.scandir(bstack1ll111l11l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l11111_opy_:
                        self.logger.info(bstack1ll1l_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᗗ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1ll1l_opy_ (u"ࠨࠢᗘ")
                        log_entry = bstack1ll11lll111_opy_(
                            kind=bstack1ll1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᗙ"),
                            message=bstack1ll1l_opy_ (u"ࠣࠤᗚ"),
                            level=bstack1ll1l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᗛ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11ll11ll_opy_=entry.stat().st_size,
                            bstack1l1llllllll_opy_=bstack1ll1l_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᗜ"),
                            bstack1ll1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll11llll1l_opy_=hook.get(TestFramework.bstack1ll1l1ll1ll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l11111_opy_.add(abs_path)
        hook[bstack1ll1l_opy_ (u"ࠦࡱࡵࡧࡴࠤᗝ")] = logs
    def bstack1ll1l1ll111_opy_(
        self,
        bstack1ll1111111l_opy_: bstack1lll1l1l1ll_opy_,
        entries: List[bstack1ll11lll111_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤᗞ"))
        req.platform_index = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1lllllllll1_opy_)
        req.execution_context.hash = str(bstack1ll1111111l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1111111l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1111111l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1llll11llll_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.uuid = entry.bstack1ll11l11lll_opy_
            log_entry.test_framework_state = bstack1ll1111111l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1ll1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᗟ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1ll1l_opy_ (u"ࠢࠣᗠ")
            if entry.kind == bstack1ll1l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᗡ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11ll11ll_opy_
                log_entry.file_path = entry.bstack1ll1ll_opy_
        def bstack1ll1l1ll1l1_opy_():
            bstack1l11l11lll_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.LogCreatedEvent(req)
                bstack1ll1111111l_opy_.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᗢ"), datetime.now() - bstack1l11l11lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡻࡾࠤᗣ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l1ll1l1_opy_)
    def __1ll11ll1ll1_opy_(self, instance) -> None:
        bstack1ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡎࡲࡥࡩࡹࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡤࡪࡥࡷࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡩࡵࡴࡶࡲࡱࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡪࡷࡵ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡧ࡮ࡥࠢࡸࡴࡩࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡶࡸࡦࡺࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᗤ")
        bstack1ll11l1ll1l_opy_ = {bstack1ll1l_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢᗥ"): bstack1l1lllll1l1_opy_.bstack1ll11l1111l_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll1l1l11ll_opy_(instance, bstack1ll11l1ll1l_opy_)
    @staticmethod
    def bstack1ll111ll11l_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll111lll11_opy_: str):
        bstack1ll1l1ll11l_opy_ = (
            bstack1l1l111ll11_opy_.bstack1ll11111lll_opy_
            if bstack1ll111lll11_opy_ == bstack1l1l111ll11_opy_.bstack1ll1l1111ll_opy_
            else bstack1l1l111ll11_opy_.bstack1ll11ll1l1l_opy_
        )
        bstack1ll11l11l1l_opy_ = TestFramework.get_state(instance, bstack1ll111lll11_opy_, None)
        bstack1ll111111ll_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll11l_opy_, None) if bstack1ll11l11l1l_opy_ else None
        return (
            bstack1ll111111ll_opy_[bstack1ll11l11l1l_opy_][-1]
            if isinstance(bstack1ll111111ll_opy_, dict) and len(bstack1ll111111ll_opy_.get(bstack1ll11l11l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1111l111_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll111lll11_opy_: str):
        hook = bstack1l1l111ll11_opy_.bstack1ll111ll11l_opy_(instance, bstack1ll111lll11_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11ll111l_opy_, []).clear()
    @staticmethod
    def __1l1llll1ll1_opy_(instance: bstack1lll1l1l1ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1ll1l_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡩ࡯ࡳࡦࡶࠦᗦ"), None)):
            return
        if os.getenv(bstack1ll1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡌࡐࡉࡖࠦᗧ"), bstack1ll1l_opy_ (u"ࠣ࠳ࠥᗨ")) != bstack1ll1l_opy_ (u"ࠤ࠴ࠦᗩ"):
            bstack1l1l111ll11_opy_.logger.warning(bstack1ll1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳ࡫ࡱ࡫ࠥࡩࡡࡱ࡮ࡲ࡫ࠧᗪ"))
            return
        bstack1ll1111ll11_opy_ = {
            bstack1ll1l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᗫ"): (bstack1l1l111ll11_opy_.bstack1ll111l1lll_opy_, bstack1l1l111ll11_opy_.bstack1ll11ll1l1l_opy_),
            bstack1ll1l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᗬ"): (bstack1l1l111ll11_opy_.bstack1ll1l1111ll_opy_, bstack1l1l111ll11_opy_.bstack1ll11111lll_opy_),
        }
        for when in (bstack1ll1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᗭ"), bstack1ll1l_opy_ (u"ࠢࡤࡣ࡯ࡰࠧᗮ"), bstack1ll1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᗯ")):
            bstack1ll1l11111l_opy_ = args[1].get_records(when)
            if not bstack1ll1l11111l_opy_:
                continue
            records = [
                bstack1ll11lll111_opy_(
                    kind=TestFramework.bstack1ll11l1l11l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1ll1l_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩࠧᗰ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1ll1l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡧࠦᗱ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l11111l_opy_
                if isinstance(getattr(r, bstack1ll1l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧᗲ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1l111ll1_opy_, bstack1ll1l1ll11l_opy_ = bstack1ll1111ll11_opy_.get(when, (None, None))
            bstack1ll1l111l11_opy_ = TestFramework.get_state(instance, bstack1ll1l111ll1_opy_, None) if bstack1ll1l111ll1_opy_ else None
            bstack1ll111111ll_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll11l_opy_, None) if bstack1ll1l111l11_opy_ else None
            if isinstance(bstack1ll111111ll_opy_, dict) and len(bstack1ll111111ll_opy_.get(bstack1ll1l111l11_opy_, [])) > 0:
                hook = bstack1ll111111ll_opy_[bstack1ll1l111l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11ll111l_opy_ in hook:
                    hook[TestFramework.bstack1ll11ll111l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l1l1111_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l111ll11_opy_.__1ll1l1l1l1l_opy_(test.location) if hasattr(test, bstack1ll1l_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᗳ")) else getattr(test, bstack1ll1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᗴ"), None)
        test_name = test.name if hasattr(test, bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᗵ")) else None
        bstack1l1lllll11l_opy_ = test.fspath.strpath if hasattr(test, bstack1ll1l_opy_ (u"ࠣࡨࡶࡴࡦࡺࡨࠣᗶ")) and test.fspath else None
        if not test_id or not test_name or not bstack1l1lllll11l_opy_:
            return None
        code = None
        if hasattr(test, bstack1ll1l_opy_ (u"ࠤࡲࡦ࡯ࠨᗷ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll1ll1l_opy_ = []
        try:
            bstack11llll1ll1l_opy_ = bstack1l11llll_opy_.bstack1l111lll_opy_(test)
        except:
            bstack1l1l111ll11_opy_.logger.warning(bstack1ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡹ࡫ࡳࡵࠢࡶࡧࡴࡶࡥࡴ࠮ࠣࡸࡪࡹࡴࠡࡵࡦࡳࡵ࡫ࡳࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡵࡩࡸࡵ࡬ࡷࡧࡧࠤ࡮ࡴࠠࡄࡎࡌࠦᗸ"))
        return {
            TestFramework.bstack1llll11ll1l_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11l1llll_opy_: test_id,
            TestFramework.bstack1ll1l11l11l_opy_: test_name,
            TestFramework.bstack1ll111l11ll_opy_: getattr(test, bstack1ll1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᗹ"), None),
            TestFramework.bstack1ll1ll11111_opy_: bstack1l1lllll11l_opy_,
            TestFramework.bstack1ll1l1lll11_opy_: bstack1l1l111ll11_opy_.__1ll111l1ll1_opy_(test),
            TestFramework.bstack1ll11l111l1_opy_: code,
            TestFramework.bstack1lll1l11l1l_opy_: TestFramework.bstack1ll111ll1l1_opy_,
            TestFramework.bstack1lll111llll_opy_: test_id,
            TestFramework.bstack1l1111l1l11_opy_: bstack11llll1ll1l_opy_
        }
    @staticmethod
    def __1ll111l1ll1_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1ll1l_opy_ (u"ࠧࡵࡷ࡯ࡡࡰࡥࡷࡱࡥࡳࡵࠥᗺ"), [])
            markers.extend([getattr(m, bstack1ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᗻ"), None) for m in own_markers if getattr(m, bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᗼ"), None)])
            current = getattr(current, bstack1ll1l_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᗽ"), None)
        return markers
    @staticmethod
    def __1ll1l1l1l1l_opy_(location):
        return bstack1ll1l_opy_ (u"ࠤ࠽࠾ࠧᗾ").join(filter(lambda x: isinstance(x, str), location))