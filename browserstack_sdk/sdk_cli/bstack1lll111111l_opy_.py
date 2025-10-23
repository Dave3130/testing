# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
    bstack1lll1111lll_opy_,
    bstack1llll11l11l_opy_,
    bstack1lll11l1ll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll1l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_, bstack1llll11111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lll11ll1l1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l11111_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11111ll_opy_(bstack1lll11ll1l1_opy_):
    bstack1lll1l1111l_opy_ = bstack11lll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᅺ")
    bstack1llll111ll1_opy_ = bstack11lll1_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅻ")
    bstack1lll1l1llll_opy_ = bstack11lll1_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅼ")
    bstack1lll1ll1l11_opy_ = bstack11lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅽ")
    bstack1lll1lll1l1_opy_ = bstack11lll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᅾ")
    bstack1lll1l111ll_opy_ = bstack11lll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᅿ")
    bstack1lll1l11l1l_opy_ = bstack11lll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᆀ")
    bstack1lll1ll1lll_opy_ = bstack11lll1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᆁ")
    def __init__(self):
        super().__init__(bstack1llll111l1l_opy_=self.bstack1lll1l1111l_opy_, frameworks=[bstack1lllll1l11l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1llll11l111_opy_.POST), self.bstack1lll1111l1l_opy_)
        TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.PRE), self.bstack1lll1l11lll_opy_)
        TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.POST), self.bstack1lll11lll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll111l111_opy_ = self.bstack1lll111lll1_opy_(instance.context)
        if not bstack1lll111l111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᆂ") + str(bstack1llll1lll1l_opy_) + bstack11lll1_opy_ (u"ࠥࠦᆃ"))
        f.bstack1lllll11l11_opy_(instance, bstack1lll11111ll_opy_.bstack1llll111ll1_opy_, bstack1lll111l111_opy_)
        bstack1lll111llll_opy_ = self.bstack1lll111lll1_opy_(instance.context, bstack1lll111ll1l_opy_=False)
        f.bstack1lllll11l11_opy_(instance, bstack1lll11111ll_opy_.bstack1lll1l1llll_opy_, bstack1lll111llll_opy_)
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l1l_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1l11l1l_opy_, False):
            self.__1lll11l1111_opy_(f,instance,bstack1llll1lll1l_opy_)
    def bstack1lll11lll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l1l_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1l11l1l_opy_, False):
            self.__1lll11l1111_opy_(f, instance, bstack1llll1lll1l_opy_)
        if not f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1ll1lll_opy_, False):
            self.__1lll111ll11_opy_(f, instance, bstack1llll1lll1l_opy_)
    def bstack1lll11111l1_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll111l1ll_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1ll1lll_opy_, False):
            return
        driver.execute_script(
            bstack11lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᆄ").format(
                json.dumps(
                    {
                        bstack11lll1_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᆅ"): bstack11lll1_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᆆ"),
                        bstack11lll1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆇ"): {bstack11lll1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᆈ"): result},
                    }
                )
            )
        )
        f.bstack1lllll11l11_opy_(instance, bstack1lll11111ll_opy_.bstack1lll1ll1lll_opy_, True)
    def bstack1lll111lll1_opy_(self, context: bstack1lll11l1ll1_opy_, bstack1lll111ll1l_opy_= True):
        if bstack1lll111ll1l_opy_:
            bstack1lll111l111_opy_ = self.bstack1lll1l1ll1l_opy_(context, reverse=True)
        else:
            bstack1lll111l111_opy_ = self.bstack1lll1lll11l_opy_(context, reverse=True)
        return [f for f in bstack1lll111l111_opy_ if f[1].state != bstack1lllll111ll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11l1111lll_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def __1lll111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11lll1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᆉ")).get(bstack11lll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᆊ")):
            bstack1lll111l111_opy_ = f.get_state(instance, bstack1lll11111ll_opy_.bstack1llll111ll1_opy_, [])
            if not bstack1lll111l111_opy_:
                self.logger.debug(bstack11lll1_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆋ") + str(bstack1llll1lll1l_opy_) + bstack11lll1_opy_ (u"ࠧࠨᆌ"))
                return
            driver = bstack1lll111l111_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1ll111l_opy_, None)
            if not status:
                self.logger.debug(bstack11lll1_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆍ") + str(bstack1llll1lll1l_opy_) + bstack11lll1_opy_ (u"ࠢࠣᆎ"))
                return
            bstack1lll1lll111_opy_ = {bstack11lll1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᆏ"): status.lower()}
            bstack1lll11lllll_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1lll1_opy_, None)
            if status.lower() == bstack11lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᆐ") and bstack1lll11lllll_opy_ is not None:
                bstack1lll1lll111_opy_[bstack11lll1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᆑ")] = bstack1lll11lllll_opy_[0][bstack11lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᆒ")][0] if isinstance(bstack1lll11lllll_opy_, list) else str(bstack1lll11lllll_opy_)
            driver.execute_script(
                bstack11lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆓ").format(
                    json.dumps(
                        {
                            bstack11lll1_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆔ"): bstack11lll1_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᆕ"),
                            bstack11lll1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆖ"): bstack1lll1lll111_opy_,
                        }
                    )
                )
            )
            f.bstack1lllll11l11_opy_(instance, bstack1lll11111ll_opy_.bstack1lll1ll1lll_opy_, True)
    @measure(event_name=EVENTS.bstack11111l11l_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def __1lll11l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11lll1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᆗ")).get(bstack11lll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᆘ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll111l1l1_opy_, None)
            if not test_name:
                self.logger.debug(bstack11lll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᆙ"))
                return
            bstack1lll111l111_opy_ = f.get_state(instance, bstack1lll11111ll_opy_.bstack1llll111ll1_opy_, [])
            if not bstack1lll111l111_opy_:
                self.logger.debug(bstack11lll1_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆚ") + str(bstack1llll1lll1l_opy_) + bstack11lll1_opy_ (u"ࠨࠢᆛ"))
                return
            for bstack1lll1111111_opy_, bstack1lll1111ll1_opy_ in bstack1lll111l111_opy_:
                if not bstack1lllll1l11l_opy_.bstack1lll111l1ll_opy_(bstack1lll1111ll1_opy_):
                    continue
                driver = bstack1lll1111111_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆜ").format(
                        json.dumps(
                            {
                                bstack11lll1_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆝ"): bstack11lll1_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᆞ"),
                                bstack11lll1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆟ"): {bstack11lll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆠ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1lllll11l11_opy_(instance, bstack1lll11111ll_opy_.bstack1lll1l11l1l_opy_, True)
    def bstack1lll11llll1_opy_(
        self,
        instance: bstack1llll11111l_opy_,
        f: TestFramework,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l1l_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        bstack1lll111l111_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11111ll_opy_.bstack1llll111ll1_opy_, [])]
        if not bstack1lll111l111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆡ"))
            return
        if not bstack1lll1l11111_opy_():
            self.logger.debug(bstack11lll1_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᆢ"))
            return
        for bstack1lll1111l11_opy_ in bstack1lll111l111_opy_:
            driver = bstack1lll1111l11_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11lll1_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᆣ") + str(timestamp)
            driver.execute_script(
                bstack11lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆤ").format(
                    json.dumps(
                        {
                            bstack11lll1_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆥ"): bstack11lll1_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᆦ"),
                            bstack11lll1_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆧ"): {
                                bstack11lll1_opy_ (u"ࠧࡺࡹࡱࡧࠥᆨ"): bstack11lll1_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᆩ"),
                                bstack11lll1_opy_ (u"ࠢࡥࡣࡷࡥࠧᆪ"): data,
                                bstack11lll1_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᆫ"): bstack11lll1_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᆬ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1ll1ll1_opy_(
        self,
        instance: bstack1llll11111l_opy_,
        f: TestFramework,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l1l_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        keys = [
            bstack1lll11111ll_opy_.bstack1llll111ll1_opy_,
            bstack1lll11111ll_opy_.bstack1lll1l1llll_opy_,
        ]
        bstack1lll111l111_opy_ = []
        for key in keys:
            bstack1lll111l111_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll111l111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧ࡮ࡺࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆭ"))
            return
        if f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1l111ll_opy_, False):
            self.logger.debug(bstack11lll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡉࡂࡕࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡧࡷ࡫ࡡࡵࡧࡧࠦᆮ"))
            return
        self.bstack1llll1ll1ll_opy_()
        bstack11l11lll1l_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1ll111_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        req.test_framework_state = bstack1llll1lll1l_opy_[0].name
        req.test_hook_state = bstack1llll1lll1l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
        for bstack1lll1111111_opy_, driver in bstack1lll111l111_opy_:
            try:
                webdriver = bstack1lll1111111_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11lll1_opy_ (u"ࠧ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠤ࠭ࡸࡥࡧࡧࡵࡩࡳࡩࡥࠡࡧࡻࡴ࡮ࡸࡥࡥࠫࠥᆯ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᆰ")
                    if bstack1lllll1l11l_opy_.get_state(driver, bstack1lllll1l11l_opy_.bstack1lll11l11l1_opy_, False)
                    else bstack11lll1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᆱ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll1l11l_opy_.get_state(driver, bstack1lllll1l11l_opy_.bstack1lll1l1l11l_opy_, bstack11lll1_opy_ (u"ࠣࠤᆲ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll1l11l_opy_.get_state(driver, bstack1lllll1l11l_opy_.bstack1lll1l1l1ll_opy_, bstack11lll1_opy_ (u"ࠤࠥᆳ"))
                caps = None
                if hasattr(webdriver, bstack11lll1_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᆴ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11lll1_opy_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥࡪࡩࡳࡧࡦࡸࡱࡿࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠳ࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᆵ"))
                    except Exception as e:
                        self.logger.debug(bstack11lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠻ࠢࠥᆶ") + str(e) + bstack11lll1_opy_ (u"ࠨࠢᆷ"))
                try:
                    bstack1lll11l111l_opy_ = json.dumps(caps).encode(bstack11lll1_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆸ")) if caps else bstack1lll111l11l_opy_ (u"ࠣࡽࢀࠦᆹ")
                    req.capabilities = bstack1lll11l111l_opy_
                except Exception as e:
                    self.logger.debug(bstack11lll1_opy_ (u"ࠤࡪࡩࡹࡥࡣࡣࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤࡸ࡫ࡲࡪࡣ࡯࡭ࡿ࡫ࠠࡤࡣࡳࡷࠥ࡬࡯ࡳࠢࡵࡩࡶࡻࡥࡴࡶ࠽ࠤࠧᆺ") + str(e) + bstack11lll1_opy_ (u"ࠥࠦᆻ"))
            except Exception as e:
                self.logger.error(bstack11lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡶࡨࡱ࠿ࠦࠢᆼ") + str(str(e)) + bstack11lll1_opy_ (u"ࠧࠨᆽ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l111_opy_ = f.get_state(instance, bstack1lll11111ll_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1l11111_opy_() and len(bstack1lll111l111_opy_) == 0:
            bstack1lll111l111_opy_ = f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll111l111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆾ") + str(kwargs) + bstack11lll1_opy_ (u"ࠢࠣᆿ"))
            return {}
        if len(bstack1lll111l111_opy_) > 1:
            self.logger.debug(bstack11lll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇀ") + str(kwargs) + bstack11lll1_opy_ (u"ࠤࠥᇁ"))
            return {}
        bstack1lll1111111_opy_, bstack1lll1llll11_opy_ = bstack1lll111l111_opy_[0]
        driver = bstack1lll1111111_opy_()
        if not driver:
            self.logger.debug(bstack11lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇂ") + str(kwargs) + bstack11lll1_opy_ (u"ࠦࠧᇃ"))
            return {}
        capabilities = f.get_state(bstack1lll1llll11_opy_, bstack1lllll1l11l_opy_.bstack1lll11ll1ll_opy_)
        if not capabilities:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇄ") + str(kwargs) + bstack11lll1_opy_ (u"ࠨࠢᇅ"))
            return {}
        return capabilities.get(bstack11lll1_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧᇆ"), {})
    def bstack1lll1ll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l111_opy_ = f.get_state(instance, bstack1lll11111ll_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1l11111_opy_() and len(bstack1lll111l111_opy_) == 0:
            bstack1lll111l111_opy_ = f.get_state(instance, bstack1lll11111ll_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll111l111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇇ") + str(kwargs) + bstack11lll1_opy_ (u"ࠤࠥᇈ"))
            return
        if len(bstack1lll111l111_opy_) > 1:
            self.logger.debug(bstack11lll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇉ") + str(kwargs) + bstack11lll1_opy_ (u"ࠦࠧᇊ"))
        bstack1lll1111111_opy_, bstack1lll1llll11_opy_ = bstack1lll111l111_opy_[0]
        driver = bstack1lll1111111_opy_()
        if not driver:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇋ") + str(kwargs) + bstack11lll1_opy_ (u"ࠨࠢᇌ"))
            return
        return driver