# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llll1ll111_opy_, bstack1llllll1111_opy_, bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1lll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1llllll_opy_, bstack1lll1l1llll_opy_, bstack1lll1l1lll1_opy_, bstack1ll11111111_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll1lll_opy_, bstack1ll11ll1l11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1l11l1_opy_ = [bstack1l111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᏍ"), bstack1l111ll_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᏎ"), bstack1l111ll_opy_ (u"ࠥࡧࡴࡴࡦࡪࡩࠥᏏ"), bstack1l111ll_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࠧᏐ"), bstack1l111ll_opy_ (u"ࠧࡶࡡࡵࡪࠥᏑ")]
bstack1l1llll1lll_opy_ = bstack1ll11ll1l11_opy_()
bstack1ll111111l1_opy_ = bstack1l111ll_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᏒ")
bstack1l11l111lll_opy_ = {
    bstack1l111ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡊࡶࡨࡱࠧᏓ"): bstack1l11l1l11l1_opy_,
    bstack1l111ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡒࡤࡧࡰࡧࡧࡦࠤᏔ"): bstack1l11l1l11l1_opy_,
    bstack1l111ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡐࡳࡩࡻ࡬ࡦࠤᏕ"): bstack1l11l1l11l1_opy_,
    bstack1l111ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡇࡱࡧࡳࡴࠤᏖ"): bstack1l11l1l11l1_opy_,
    bstack1l111ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡋࡻ࡮ࡤࡶ࡬ࡳࡳࠨᏗ"): bstack1l11l1l11l1_opy_
    + [
        bstack1l111ll_opy_ (u"ࠧࡵࡲࡪࡩ࡬ࡲࡦࡲ࡮ࡢ࡯ࡨࠦᏘ"),
        bstack1l111ll_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᏙ"),
        bstack1l111ll_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࡪࡰࡩࡳࠧᏚ"),
        bstack1l111ll_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᏛ"),
        bstack1l111ll_opy_ (u"ࠤࡦࡥࡱࡲࡳࡱࡧࡦࠦᏜ"),
        bstack1l111ll_opy_ (u"ࠥࡧࡦࡲ࡬ࡰࡤ࡭ࠦᏝ"),
        bstack1l111ll_opy_ (u"ࠦࡸࡺࡡࡳࡶࠥᏞ"),
        bstack1l111ll_opy_ (u"ࠧࡹࡴࡰࡲࠥᏟ"),
        bstack1l111ll_opy_ (u"ࠨࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠣᏠ"),
        bstack1l111ll_opy_ (u"ࠢࡸࡪࡨࡲࠧᏡ"),
    ],
    bstack1l111ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤ࡭ࡳ࠴ࡓࡦࡵࡶ࡭ࡴࡴࠢᏢ"): [bstack1l111ll_opy_ (u"ࠤࡶࡸࡦࡸࡴࡱࡣࡷ࡬ࠧᏣ"), bstack1l111ll_opy_ (u"ࠥࡸࡪࡹࡴࡴࡨࡤ࡭ࡱ࡫ࡤࠣᏤ"), bstack1l111ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࡦࡳࡱࡲࡥࡤࡶࡨࡨࠧᏥ"), bstack1l111ll_opy_ (u"ࠧ࡯ࡴࡦ࡯ࡶࠦᏦ")],
    bstack1l111ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡣࡰࡰࡩ࡭࡬࠴ࡃࡰࡰࡩ࡭࡬ࠨᏧ"): [bstack1l111ll_opy_ (u"ࠢࡪࡰࡹࡳࡨࡧࡴࡪࡱࡱࡣࡵࡧࡲࡢ࡯ࡶࠦᏨ"), bstack1l111ll_opy_ (u"ࠣࡣࡵ࡫ࡸࠨᏩ")],
    bstack1l111ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡋ࡯ࡸࡵࡷࡵࡩࡉ࡫ࡦࠣᏪ"): [bstack1l111ll_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᏫ"), bstack1l111ll_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧᏬ"), bstack1l111ll_opy_ (u"ࠧ࡬ࡵ࡯ࡥࠥᏭ"), bstack1l111ll_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᏮ"), bstack1l111ll_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤᏯ"), bstack1l111ll_opy_ (u"ࠣ࡫ࡧࡷࠧᏰ")],
    bstack1l111ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡘࡻࡢࡓࡧࡴࡹࡪࡹࡴࠣᏱ"): [bstack1l111ll_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣᏲ"), bstack1l111ll_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࠥᏳ"), bstack1l111ll_opy_ (u"ࠧࡶࡡࡳࡣࡰࡣ࡮ࡴࡤࡦࡺࠥᏴ")],
    bstack1l111ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡲࡶࡰࡱࡩࡷ࠴ࡃࡢ࡮࡯ࡍࡳ࡬࡯ࠣᏵ"): [bstack1l111ll_opy_ (u"ࠢࡸࡪࡨࡲࠧ᏶"), bstack1l111ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࠣ᏷")],
    bstack1l111ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥࡷࡱ࠮ࡴࡶࡵࡹࡨࡺࡵࡳࡧࡶ࠲ࡓࡵࡤࡦࡍࡨࡽࡼࡵࡲࡥࡵࠥᏸ"): [bstack1l111ll_opy_ (u"ࠥࡲࡴࡪࡥࠣᏹ"), bstack1l111ll_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᏺ")],
    bstack1l111ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡎࡣࡵ࡯ࠧᏻ"): [bstack1l111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᏼ"), bstack1l111ll_opy_ (u"ࠢࡢࡴࡪࡷࠧᏽ"), bstack1l111ll_opy_ (u"ࠣ࡭ࡺࡥࡷ࡭ࡳࠣ᏾")],
}
_1ll1l1ll111_opy_ = set()
class bstack1l1l11l11l1_opy_(bstack1lllll111l1_opy_):
    bstack1l11l1ll1ll_opy_ = bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡧࡩࡩࡷࡸࡥࡥࠤ᏿")
    bstack1l11l11l1ll_opy_ = bstack1l111ll_opy_ (u"ࠥࡍࡓࡌࡏࠣ᐀")
    bstack1l11l1lll11_opy_ = bstack1l111ll_opy_ (u"ࠦࡊࡘࡒࡐࡔࠥᐁ")
    bstack1l11ll11111_opy_: Callable
    bstack1l111ll1lll_opy_: Callable
    def __init__(self, bstack1l1l1l111l1_opy_, bstack1ll1ll1ll11_opy_):
        super().__init__()
        self.bstack1l11l111ll1_opy_ = bstack1ll1ll1ll11_opy_
        if os.getenv(bstack1l111ll_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡔ࠷࠱࡚ࠤᐂ"), bstack1l111ll_opy_ (u"ࠨ࠱ࠣᐃ")) != bstack1l111ll_opy_ (u"ࠢ࠲ࠤᐄ") or not self.is_enabled():
            self.logger.warning(bstack1l111ll_opy_ (u"ࠣࠤᐅ") + str(self.__class__.__name__) + bstack1l111ll_opy_ (u"ࠤࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠧᐆ"))
            return
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.PRE), self.bstack1lll1lll11l_opy_)
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.POST), self.bstack1lll1l1ll1l_opy_)
        for event in bstack1lll1llllll_opy_:
            for state in bstack1lll1l1lll1_opy_:
                TestFramework.bstack1lllll1l111_opy_((event, state), self.bstack1l111ll1l1l_opy_)
        bstack1l1l1l111l1_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllllll11l_opy_, bstack1lllll11l11_opy_.POST), self.bstack1l111ll1ll1_opy_)
        self.bstack1l11ll11111_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l1111ll_opy_(bstack1l1l11l11l1_opy_.bstack1l11l11l1ll_opy_, self.bstack1l11ll11111_opy_)
        self.bstack1l111ll1lll_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l1111ll_opy_(bstack1l1l11l11l1_opy_.bstack1l11l1lll11_opy_, self.bstack1l111ll1lll_opy_)
        self.bstack1l11l1lll1l_opy_ = builtins.print
        builtins.print = self.bstack1l11l11ll11_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l111ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll1l11ll1l_opy_() and instance:
            bstack1l11l11ll1l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1l1l1_opy_
            if test_framework_state == bstack1lll1llllll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1llllll_opy_.LOG:
                bstack11111ll1ll_opy_ = datetime.now()
                entries = f.bstack1l1llll1111_opy_(instance, bstack1lllll1l1l1_opy_)
                if entries:
                    self.bstack1ll1l1l1lll_opy_(instance, entries)
                    instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࠥᐇ"), datetime.now() - bstack11111ll1ll_opy_)
                    f.bstack1ll11lll11l_opy_(instance, bstack1lllll1l1l1_opy_)
                instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᐈ"), datetime.now() - bstack1l11l11ll1l_opy_)
                return # do not send this event with the bstack1l11l111111_opy_ bstack1l111lll111_opy_
            elif (
                test_framework_state == bstack1lll1llllll_opy_.TEST
                and test_hook_state == bstack1lll1l1lll1_opy_.POST
                and not f.bstack1llll1l1111_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)
            ):
                self.logger.warning(bstack1l111ll_opy_ (u"ࠧࡪࡲࡰࡲࡳ࡭ࡳ࡭ࠠࡥࡷࡨࠤࡹࡵࠠ࡭ࡣࡦ࡯ࠥࡵࡦࠡࡴࡨࡷࡺࡲࡴࡴࠢࠥᐉ") + str(TestFramework.bstack1llll1l1111_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)) + bstack1l111ll_opy_ (u"ࠨࠢᐊ"))
                f.bstack1lllll1ll1l_opy_(instance, bstack1l1l11l11l1_opy_.bstack1l11l1ll1ll_opy_, True)
                return # do not send this event bstack1l11l11l111_opy_ bstack1l11l1ll111_opy_
            elif (
                f.get_state(instance, bstack1l1l11l11l1_opy_.bstack1l11l1ll1ll_opy_, False)
                and test_framework_state == bstack1lll1llllll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1l1lll1_opy_.POST
                and f.bstack1llll1l1111_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)
            ):
                self.logger.warning(bstack1l111ll_opy_ (u"ࠢࡪࡰ࡭ࡩࡨࡺࡩ࡯ࡩࠣࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡖࡈࡗ࡙࠲ࠠࡕࡧࡶࡸࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡑࡑࡖࡘࠥࠨᐋ") + str(TestFramework.bstack1llll1l1111_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)) + bstack1l111ll_opy_ (u"ࠣࠤᐌ"))
                self.bstack1l111ll1l1l_opy_(f, instance, (bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.POST), *args, **kwargs)
            bstack11111ll1ll_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l111ll1l11_opy_ = sorted(
                filter(lambda x: x.get(bstack1l111ll_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᐍ"), None), data.pop(bstack1l111ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᐎ"), {}).values()),
                key=lambda x: x[bstack1l111ll_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᐏ")],
            )
            if bstack1lll11111l1_opy_.bstack1lll11llll1_opy_ in data:
                data.pop(bstack1lll11111l1_opy_.bstack1lll11llll1_opy_)
            data.update({bstack1l111ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᐐ"): bstack1l111ll1l11_opy_})
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᐑ"), datetime.now() - bstack11111ll1ll_opy_)
            bstack11111ll1ll_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l1l1ll1_opy_)
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠢ࡫ࡵࡲࡲ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᐒ"), datetime.now() - bstack11111ll1ll_opy_)
            self.bstack1l111lll111_opy_(instance, bstack1lllll1l1l1_opy_, event_json=event_json)
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦᐓ"), datetime.now() - bstack1l11l11ll1l_opy_)
    def bstack1lll1lll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111llll1l_opy_ import bstack1llll11l1ll_opy_
        bstack1ll111ll111_opy_ = bstack1llll11l1ll_opy_.bstack1ll1l11l1ll_opy_(EVENTS.bstack11l1l1111_opy_.value)
        self.bstack1l11l111ll1_opy_.bstack1lll1l1ll11_opy_(instance, f, bstack1lllll1l1l1_opy_, *args, **kwargs)
        bstack1llll11l1ll_opy_.end(EVENTS.bstack11l1l1111_opy_.value, bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᐔ"), bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᐕ"), status=True, failure=None, test_name=None)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l111ll1_opy_.bstack1llll111l11_opy_(instance, f, bstack1lllll1l1l1_opy_, *args, **kwargs)
        self.bstack1l11l1l1111_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l111l11_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def bstack1l11l1l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡗࡪࡹࡳࡪࡱࡱࡉࡻ࡫࡮ࡵࠢࡪࡖࡕࡉࠠࡤࡣ࡯ࡰ࠿ࠦࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠢᐖ"))
            return
        bstack11111ll1ll_opy_ = datetime.now()
        try:
            r = self.bstack1lllll1lll1_opy_.TestSessionEvent(req)
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡦࡸࡨࡲࡹࠨᐗ"), datetime.now() - bstack11111ll1ll_opy_)
            f.bstack1lllll1ll1l_opy_(instance, self.bstack1l11l111ll1_opy_.bstack1llll111lll_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l111ll_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᐘ") + str(r) + bstack1l111ll_opy_ (u"ࠢࠣᐙ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᐚ") + str(e) + bstack1l111ll_opy_ (u"ࠤࠥᐛ"))
            traceback.print_exc()
            raise e
    def bstack1l111ll1ll1_opy_(
        self,
        f: bstack1lllllll1l1_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        _1l111llllll_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllllll1l1_opy_.bstack1l1lll11l1l_opy_(method_name):
            return
        if f.bstack1l1ll1ll1ll_opy_(*args) == bstack1lllllll1l1_opy_.bstack1l11l1l111l_opy_:
            bstack1l11l11ll1l_opy_ = datetime.now()
            screenshot = result.get(bstack1l111ll_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤᐜ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1l111ll_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠢ࡬ࡱࡦ࡭ࡥࠡࡤࡤࡷࡪ࠼࠴ࠡࡵࡷࡶࠧᐝ"))
                return
            bstack1ll111l11ll_opy_ = self.bstack1l11l11lll1_opy_(instance)
            if bstack1ll111l11ll_opy_:
                entry = bstack1ll11111111_opy_(TestFramework.bstack1l11l1l1lll_opy_, screenshot)
                self.bstack1ll1l1l1lll_opy_(bstack1ll111l11ll_opy_, [entry])
                instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡࡧࡶࡨࡶࡤ࡫ࡸࡦࡥࡸࡸࡪࠨᐞ"), datetime.now() - bstack1l11l11ll1l_opy_)
            else:
                self.logger.warning(bstack1l111ll_opy_ (u"ࠨࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡥࡴࡶࠣࡪࡴࡸࠠࡸࡪ࡬ࡧ࡭ࠦࡴࡩ࡫ࡶࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡࡹࡤࡷࠥࡺࡡ࡬ࡧࡱࠤࡧࡿࠠࡥࡴ࡬ࡺࡪࡸ࠽ࠡࡽࢀࠦᐟ").format(instance.ref()))
        event = {}
        bstack1ll111l11ll_opy_ = self.bstack1l11l11lll1_opy_(instance)
        if bstack1ll111l11ll_opy_:
            self.bstack1l11l1l1l1l_opy_(event, bstack1ll111l11ll_opy_)
            if event.get(bstack1l111ll_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᐠ")):
                self.bstack1ll1l1l1lll_opy_(bstack1ll111l11ll_opy_, event[bstack1l111ll_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᐡ")])
            else:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡ࡮ࡲ࡫ࡸࠦࡦࡰࡴࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡦࡸࡨࡲࡹࠨᐢ"))
    @measure(event_name=EVENTS.bstack1l111lll1l1_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def bstack1ll1l1l1lll_opy_(
        self,
        bstack1ll111l11ll_opy_: bstack1lll1l1llll_opy_,
        entries: List[bstack1ll11111111_opy_],
    ):
        self.bstack1lllll1111l_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll111l11ll_opy_, TestFramework.bstack1llll1l1l11_opy_)
        req.execution_context.hash = str(bstack1ll111l11ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111l11ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111l11ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111l11ll_opy_, TestFramework.bstack1lll11ll1l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111l11ll_opy_, TestFramework.bstack1lll1l11111_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll111l11ll_opy_, TestFramework.bstack1llll1111ll_opy_)
            log_entry.test_framework_state = bstack1ll111l11ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l111ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᐣ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l111ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᐤ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l111ll_opy_
                log_entry.file_path = entry.bstack1lllll1l_opy_
        def bstack1ll111l1l1l_opy_():
            bstack11111ll1ll_opy_ = datetime.now()
            try:
                self.bstack1lllll1lll1_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1l1lll_opy_:
                    bstack1ll111l11ll_opy_.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᐥ"), datetime.now() - bstack11111ll1ll_opy_)
                elif entry.kind == TestFramework.bstack1l11l11l1l1_opy_:
                    bstack1ll111l11ll_opy_.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥᐦ"), datetime.now() - bstack11111ll1ll_opy_)
                else:
                    bstack1ll111l11ll_opy_.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟࡭ࡱࡪࠦᐧ"), datetime.now() - bstack11111ll1ll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l111ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᐨ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l11ll_opy_.enqueue(bstack1ll111l1l1l_opy_)
    @measure(event_name=EVENTS.bstack1l11l11111l_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def bstack1l111lll111_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        event_json=None,
    ):
        self.bstack1lllll1111l_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l1l11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll11ll1l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1lllll1l1l1_opy_[0].name
        req.test_hook_state = bstack1lllll1l1l1_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11l11ll1_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1l1llll11ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l1l1ll1_opy_)).encode(bstack1l111ll_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᐩ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll111l1l1l_opy_():
            bstack11111ll1ll_opy_ = datetime.now()
            try:
                self.bstack1lllll1lll1_opy_.TestFrameworkEvent(req)
                instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡦࡸࡨࡲࡹࠨᐪ"), datetime.now() - bstack11111ll1ll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l111ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐫ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l11ll_opy_.enqueue(bstack1ll111l1l1l_opy_)
    def bstack1l11l11lll1_opy_(self, instance: bstack1llll1ll111_opy_):
        bstack1l111llll1l_opy_ = TestFramework.bstack1l11l1ll11l_opy_(instance.context)
        for t in bstack1l111llll1l_opy_:
            bstack1lll11l1111_opy_ = TestFramework.get_state(t, bstack1lll11111l1_opy_.bstack1lll11llll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l1111_opy_):
                return t
    def bstack1l111lllll1_opy_(self, message):
        self.bstack1l11ll11111_opy_(message + bstack1l111ll_opy_ (u"ࠧࡢ࡮ࠣᐬ"))
    def log_error(self, message):
        self.bstack1l111ll1lll_opy_(message + bstack1l111ll_opy_ (u"ࠨ࡜࡯ࠤᐭ"))
    def bstack1l11l1111ll_opy_(self, level, original_func):
        def bstack1l11l1llll1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1l111ll_opy_ (u"ࠢࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥࠣᐮ") in message or bstack1l111ll_opy_ (u"ࠣ࡝ࡖࡈࡐࡉࡌࡊ࡟ࠥᐯ") in message or bstack1l111ll_opy_ (u"ࠤ࡞࡛ࡪࡨࡄࡳ࡫ࡹࡩࡷࡓ࡯ࡥࡷ࡯ࡩࡢࠨᐰ") in message:
                return return_value
            bstack1l111llll1l_opy_ = TestFramework.bstack1l11l1l11ll_opy_()
            if not bstack1l111llll1l_opy_:
                return return_value
            bstack1ll111l11ll_opy_ = next(
                (
                    instance
                    for instance in bstack1l111llll1l_opy_
                    if TestFramework.bstack1llll1l1111_opy_(instance, TestFramework.bstack1llll1111ll_opy_)
                ),
                None,
            )
            if not bstack1ll111l11ll_opy_:
                return return_value
            entry = bstack1ll11111111_opy_(TestFramework.bstack1ll1l111l11_opy_, message, level)
            self.bstack1ll1l1l1lll_opy_(bstack1ll111l11ll_opy_, [entry])
            return return_value
        return bstack1l11l1llll1_opy_
    def bstack1l11l11ll11_opy_(self):
        def bstack1l11l1111l1_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1lll1l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1l111ll_opy_ (u"ࠪࠤࠬᐱ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1l111ll_opy_ (u"ࠦࡊࡼࡥ࡯ࡶࡇ࡭ࡸࡶࡡࡵࡥ࡫ࡩࡷࡓ࡯ࡥࡷ࡯ࡩࠧᐲ") in message:
                    return
                bstack1l111llll1l_opy_ = TestFramework.bstack1l11l1l11ll_opy_()
                if not bstack1l111llll1l_opy_:
                    return
                bstack1ll111l11ll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l111llll1l_opy_
                        if TestFramework.bstack1llll1l1111_opy_(instance, TestFramework.bstack1llll1111ll_opy_)
                    ),
                    None,
                )
                if not bstack1ll111l11ll_opy_:
                    return
                entry = bstack1ll11111111_opy_(TestFramework.bstack1ll1l111l11_opy_, message, bstack1l1l11l11l1_opy_.bstack1l11l11l1ll_opy_)
                self.bstack1ll1l1l1lll_opy_(bstack1ll111l11ll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1lll1l_opy_(bstack1lll11lllll_opy_ (u"ࠧࡡࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫࡝ࠡࡎࡲ࡫ࠥࡩࡡࡱࡶࡸࡶࡪࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡦࡿࠥᐳ"))
                except:
                    pass
        return bstack1l11l1111l1_opy_
    def bstack1l11l1l1l1l_opy_(self, event: dict, instance=None) -> None:
        global _1ll1l1ll111_opy_
        levels = [bstack1l111ll_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᐴ"), bstack1l111ll_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᐵ")]
        bstack1l11l1ll1l1_opy_ = bstack1l111ll_opy_ (u"ࠣࠤᐶ")
        if instance is not None:
            try:
                bstack1l11l1ll1l1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll1111ll_opy_)
            except Exception as e:
                self.logger.warning(bstack1l111ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡹ࡮ࡪࠠࡧࡴࡲࡱࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠢᐷ").format(e))
        bstack1l111lll11l_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᐸ")]
                bstack1ll1l1l11l1_opy_ = os.path.join(bstack1l1llll1lll_opy_, (bstack1ll111111l1_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1l1l11l1_opy_):
                    self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡯ࡱࡷࠤࡵࡸࡥࡴࡧࡱࡸࠥ࡬࡯ࡳࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡔࡦࡵࡷࠤࡦࡴࡤࠡࡄࡸ࡭ࡱࡪࠠ࡭ࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᐹ").format(bstack1ll1l1l11l1_opy_))
                    continue
                file_names = os.listdir(bstack1ll1l1l11l1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1l1l11l1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1l1ll111_opy_:
                        self.logger.info(bstack1l111ll_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᐺ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1lllll_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1lllll_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1l111ll_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᐻ"):
                                entry = bstack1ll11111111_opy_(
                                    kind=bstack1l111ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᐼ"),
                                    message=bstack1l111ll_opy_ (u"ࠣࠤᐽ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11l111ll_opy_=file_size,
                                    bstack1ll111lllll_opy_=bstack1l111ll_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᐾ"),
                                    bstack1lllll1l_opy_=os.path.abspath(file_path),
                                    bstack1111ll1lll_opy_=bstack1l11l1ll1l1_opy_
                                )
                            elif level == bstack1l111ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᐿ"):
                                entry = bstack1ll11111111_opy_(
                                    kind=bstack1l111ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᑀ"),
                                    message=bstack1l111ll_opy_ (u"ࠧࠨᑁ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11l111ll_opy_=file_size,
                                    bstack1ll111lllll_opy_=bstack1l111ll_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᑂ"),
                                    bstack1lllll1l_opy_=os.path.abspath(file_path),
                                    bstack1ll1l1l1ll1_opy_=bstack1l11l1ll1l1_opy_
                                )
                            bstack1l111lll11l_opy_.append(entry)
                            _1ll1l1ll111_opy_.add(abs_path)
                        except Exception as bstack1l11l11l11l_opy_:
                            self.logger.error(bstack1l111ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡶࡦ࡯ࡳࡦࡦࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᑃ").format(bstack1l11l11l11l_opy_))
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡷࡧࡩࡴࡧࡧࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᑄ").format(e))
        event[bstack1l111ll_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᑅ")] = bstack1l111lll11l_opy_
class bstack1l11l1l1ll1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l111lll1ll_opy_ = set()
        kwargs[bstack1l111ll_opy_ (u"ࠥࡷࡰ࡯ࡰ࡬ࡧࡼࡷࠧᑆ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l11llll_opy_(obj, self.bstack1l111lll1ll_opy_)
def bstack1l11l1l1l11_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l11llll_opy_(obj, bstack1l111lll1ll_opy_=None, max_depth=3):
    if bstack1l111lll1ll_opy_ is None:
        bstack1l111lll1ll_opy_ = set()
    if id(obj) in bstack1l111lll1ll_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l111lll1ll_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l111llll11_opy_ = TestFramework.bstack1l1lll1lll1_opy_(obj)
    bstack1l11l111l1l_opy_ = next((k.lower() in bstack1l111llll11_opy_.lower() for k in bstack1l11l111lll_opy_.keys()), None)
    if bstack1l11l111l1l_opy_:
        obj = TestFramework.bstack1ll11ll11ll_opy_(obj, bstack1l11l111lll_opy_[bstack1l11l111l1l_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l111ll_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢᑇ")):
            keys = getattr(obj, bstack1l111ll_opy_ (u"ࠧࡥ࡟ࡴ࡮ࡲࡸࡸࡥ࡟ࠣᑈ"), [])
        elif hasattr(obj, bstack1l111ll_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣᑉ")):
            keys = getattr(obj, bstack1l111ll_opy_ (u"ࠢࡠࡡࡧ࡭ࡨࡺ࡟ࡠࠤᑊ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l111ll_opy_ (u"ࠣࡡࠥᑋ"))}
        if not obj and bstack1l111llll11_opy_ == bstack1l111ll_opy_ (u"ࠤࡳࡥࡹ࡮࡬ࡪࡤ࠱ࡔࡴࡹࡩࡹࡒࡤࡸ࡭ࠨᑌ"):
            obj = {bstack1l111ll_opy_ (u"ࠥࡴࡦࡺࡨࠣᑍ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l1l1l11_opy_(key) or str(key).startswith(bstack1l111ll_opy_ (u"ࠦࡤࠨᑎ")):
            continue
        if value is not None and bstack1l11l1l1l11_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l11llll_opy_(value, bstack1l111lll1ll_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l11llll_opy_(o, bstack1l111lll1ll_opy_, max_depth) for o in value]))
    return result or None