# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
    bstack1lll11ll1l1_opy_,
    bstack111111lll1_opy_,
    bstack1llll11l111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lllll11ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_, bstack1llll1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1l1_opy_ import bstack1lll1l1llll_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1l1l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11lll1l_opy_(bstack1lll1l1llll_opy_):
    bstack1lll1l11l1l_opy_ = bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨᅝ")
    bstack1lll1ll11l1_opy_ = bstack1ll11_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᅞ")
    bstack1lll1l11lll_opy_ = bstack1ll11_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅟ")
    bstack1lll1l111l1_opy_ = bstack1ll11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᅠ")
    bstack1lll1lll11l_opy_ = bstack1ll11_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣᅡ")
    bstack1lll1ll1111_opy_ = bstack1ll11_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᅢ")
    bstack1lll1lll111_opy_ = bstack1ll11_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᅣ")
    bstack1lll1l11l11_opy_ = bstack1ll11_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧᅤ")
    def __init__(self):
        super().__init__(bstack1lll1llll11_opy_=self.bstack1lll1l11l1l_opy_, frameworks=[bstack1lllll11ll1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.BEFORE_EACH, bstack1lll1ll111l_opy_.POST), self.bstack1lll11ll11l_opy_)
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1llll1l1111_opy_)
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11ll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11llll1_opy_ = self.bstack1lll11lll11_opy_(instance.context)
        if not bstack1lll11llll1_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᅥ") + str(bstack1llll1l1ll1_opy_) + bstack1ll11_opy_ (u"ࠤࠥᅦ"))
        f.bstack1llll1ll1ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, bstack1lll11llll1_opy_)
        bstack1lll11l1ll1_opy_ = self.bstack1lll11lll11_opy_(instance.context, bstack1lll111lll1_opy_=False)
        f.bstack1llll1ll1ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1lll1l11lll_opy_, bstack1lll11l1ll1_opy_)
    def bstack1llll1l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll11l_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1lll111_opy_, False):
            self.__1lll111ll1l_opy_(f,instance,bstack1llll1l1ll1_opy_)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll11l_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1lll111_opy_, False):
            self.__1lll111ll1l_opy_(f, instance, bstack1llll1l1ll1_opy_)
        if not f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1l11l11_opy_, False):
            self.__1lll11l1111_opy_(f, instance, bstack1llll1l1ll1_opy_)
    def bstack1lll11l1l11_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11l111l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1l11l11_opy_, False):
            return
        driver.execute_script(
            bstack1ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᅧ").format(
                json.dumps(
                    {
                        bstack1ll11_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᅨ"): bstack1ll11_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᅩ"),
                        bstack1ll11_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᅪ"): {bstack1ll11_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᅫ"): result},
                    }
                )
            )
        )
        f.bstack1llll1ll1ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1lll1l11l11_opy_, True)
    def bstack1lll11lll11_opy_(self, context: bstack1llll11l111_opy_, bstack1lll111lll1_opy_= True):
        if bstack1lll111lll1_opy_:
            bstack1lll11llll1_opy_ = self.bstack1lll1l1l1l1_opy_(context, reverse=True)
        else:
            bstack1lll11llll1_opy_ = self.bstack1llll11llll_opy_(context, reverse=True)
        return [f for f in bstack1lll11llll1_opy_ if f[1].state != bstack1lllllll1ll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1llll111l1_opy_, stage=STAGE.bstack1111l1111_opy_)
    def __1lll11l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᅬ")).get(bstack1ll11_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᅭ")):
            bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
            if not bstack1lll11llll1_opy_:
                self.logger.debug(bstack1ll11_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᅮ") + str(bstack1llll1l1ll1_opy_) + bstack1ll11_opy_ (u"ࠦࠧᅯ"))
                return
            driver = bstack1lll11llll1_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1llll1l_opy_, None)
            if not status:
                self.logger.debug(bstack1ll11_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅰ") + str(bstack1llll1l1ll1_opy_) + bstack1ll11_opy_ (u"ࠨࠢᅱ"))
                return
            bstack1llll111111_opy_ = {bstack1ll11_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᅲ"): status.lower()}
            bstack1llll1l111l_opy_ = f.get_state(instance, TestFramework.bstack1llll11l11l_opy_, None)
            if status.lower() == bstack1ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᅳ") and bstack1llll1l111l_opy_ is not None:
                bstack1llll111111_opy_[bstack1ll11_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᅴ")] = bstack1llll1l111l_opy_[0][bstack1ll11_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᅵ")][0] if isinstance(bstack1llll1l111l_opy_, list) else str(bstack1llll1l111l_opy_)
            driver.execute_script(
                bstack1ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᅶ").format(
                    json.dumps(
                        {
                            bstack1ll11_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅷ"): bstack1ll11_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅸ"),
                            bstack1ll11_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅹ"): bstack1llll111111_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1ll1ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1lll1l11l11_opy_, True)
    @measure(event_name=EVENTS.bstack111ll1lll_opy_, stage=STAGE.bstack1111l1111_opy_)
    def __1lll111ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᅺ")).get(bstack1ll11_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᅻ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11ll1ll_opy_, None)
            if not test_name:
                self.logger.debug(bstack1ll11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᅼ"))
                return
            bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
            if not bstack1lll11llll1_opy_:
                self.logger.debug(bstack1ll11_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᅽ") + str(bstack1llll1l1ll1_opy_) + bstack1ll11_opy_ (u"ࠧࠨᅾ"))
                return
            for bstack1lll11l11l1_opy_, bstack1lll111ll11_opy_ in bstack1lll11llll1_opy_:
                if not bstack1lllll11ll1_opy_.bstack1lll11l111l_opy_(bstack1lll111ll11_opy_):
                    continue
                driver = bstack1lll11l11l1_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1ll11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᅿ").format(
                        json.dumps(
                            {
                                bstack1ll11_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᆀ"): bstack1ll11_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᆁ"),
                                bstack1ll11_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᆂ"): {bstack1ll11_opy_ (u"ࠥࡲࡦࡳࡥࠣᆃ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1ll1ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1lll1lll111_opy_, True)
    def bstack1lll1ll1ll1_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        f: TestFramework,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll11l_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        bstack1lll11llll1_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])]
        if not bstack1lll11llll1_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦᆄ"))
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack1ll11_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᆅ"))
            return
        for bstack1lll11l11ll_opy_ in bstack1lll11llll1_opy_:
            driver = bstack1lll11l11ll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1ll11_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦᆆ") + str(timestamp)
            driver.execute_script(
                bstack1ll11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆇ").format(
                    json.dumps(
                        {
                            bstack1ll11_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆈ"): bstack1ll11_opy_ (u"ࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦᆉ"),
                            bstack1ll11_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆊ"): {
                                bstack1ll11_opy_ (u"ࠦࡹࡿࡰࡦࠤᆋ"): bstack1ll11_opy_ (u"ࠧࡇ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠤᆌ"),
                                bstack1ll11_opy_ (u"ࠨࡤࡢࡶࡤࠦᆍ"): data,
                                bstack1ll11_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࠨᆎ"): bstack1ll11_opy_ (u"ࠣࡦࡨࡦࡺ࡭ࠢᆏ")
                            }
                        }
                    )
                )
            )
    def bstack1llll1l11l1_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        f: TestFramework,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll11l_opy_(f, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
        keys = [
            bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_,
            bstack1lll11lll1l_opy_.bstack1lll1l11lll_opy_,
        ]
        bstack1lll11llll1_opy_ = []
        for key in keys:
            bstack1lll11llll1_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11llll1_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡴࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦᆐ"))
            return
        if f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll1111_opy_, False):
            self.logger.debug(bstack1ll11_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡈࡈࡔࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡦࡶࡪࡧࡴࡦࡦࠥᆑ"))
            return
        self.bstack1111111l1l_opy_()
        bstack11l1lll1l_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll111ll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1l1l11_opy_)
        req.test_framework_state = bstack1llll1l1ll1_opy_[0].name
        req.test_hook_state = bstack1llll1l1ll1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1l11ll1_opy_)
        for bstack1lll11l11l1_opy_, driver in bstack1lll11llll1_opy_:
            try:
                webdriver = bstack1lll11l11l1_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1ll11_opy_ (u"ࠦ࡜࡫ࡢࡅࡴ࡬ࡺࡪࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠣࠬࡷ࡫ࡦࡦࡴࡨࡲࡨ࡫ࠠࡦࡺࡳ࡭ࡷ࡫ࡤࠪࠤᆒ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦᆓ")
                    if bstack1lllll11ll1_opy_.get_state(driver, bstack1lllll11ll1_opy_.bstack1lll11l1lll_opy_, False)
                    else bstack1ll11_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠧᆔ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll11ll1_opy_.get_state(driver, bstack1lllll11ll1_opy_.bstack1lll1l1l1ll_opy_, bstack1ll11_opy_ (u"ࠢࠣᆕ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll11ll1_opy_.get_state(driver, bstack1lllll11ll1_opy_.bstack1lll1ll1l11_opy_, bstack1ll11_opy_ (u"ࠣࠤᆖ"))
                caps = None
                if hasattr(webdriver, bstack1ll11_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᆗ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1ll11_opy_ (u"ࠥࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤࡩ࡯ࡲࡦࡥࡷࡰࡾࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠲ࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆘ"))
                    except Exception as e:
                        self.logger.debug(bstack1ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠯ࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠺ࠡࠤᆙ") + str(e) + bstack1ll11_opy_ (u"ࠧࠨᆚ"))
                try:
                    bstack1lll111llll_opy_ = json.dumps(caps).encode(bstack1ll11_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆛ")) if caps else bstack1lll11ll111_opy_ (u"ࠢࡼࡿࠥᆜ")
                    req.capabilities = bstack1lll111llll_opy_
                except Exception as e:
                    self.logger.debug(bstack1ll11_opy_ (u"ࠣࡩࡨࡸࡤࡩࡢࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣࡷࡪࡸࡩࡢ࡮࡬ࡾࡪࠦࡣࡢࡲࡶࠤ࡫ࡵࡲࠡࡴࡨࡵࡺ࡫ࡳࡵ࠼ࠣࠦᆝ") + str(e) + bstack1ll11_opy_ (u"ࠤࠥᆞ"))
            except Exception as e:
                self.logger.error(bstack1ll11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡤࡳ࡫ࡹࡩࡷࠦࡩࡵࡧࡰ࠾ࠥࠨᆟ") + str(str(e)) + bstack1ll11_opy_ (u"ࠦࠧᆠ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1lllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1lll1ll1l1l_opy_() and len(bstack1lll11llll1_opy_) == 0:
            bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1l11lll_opy_, [])
        if not bstack1lll11llll1_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆡ") + str(kwargs) + bstack1ll11_opy_ (u"ࠨࠢᆢ"))
            return {}
        if len(bstack1lll11llll1_opy_) > 1:
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆣ") + str(kwargs) + bstack1ll11_opy_ (u"ࠣࠤᆤ"))
            return {}
        bstack1lll11l11l1_opy_, bstack1lll1lll1ll_opy_ = bstack1lll11llll1_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆥ") + str(kwargs) + bstack1ll11_opy_ (u"ࠥࠦᆦ"))
            return {}
        capabilities = f.get_state(bstack1lll1lll1ll_opy_, bstack1lllll11ll1_opy_.bstack1lll1l1lll1_opy_)
        if not capabilities:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆧ") + str(kwargs) + bstack1ll11_opy_ (u"ࠧࠨᆨ"))
            return {}
        return capabilities.get(bstack1ll11_opy_ (u"ࠨࡡ࡭ࡹࡤࡽࡸࡓࡡࡵࡥ࡫ࠦᆩ"), {})
    def bstack1lll1ll11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1lll1ll1l1l_opy_() and len(bstack1lll11llll1_opy_) == 0:
            bstack1lll11llll1_opy_ = f.get_state(instance, bstack1lll11lll1l_opy_.bstack1lll1l11lll_opy_, [])
        if not bstack1lll11llll1_opy_:
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆪ") + str(kwargs) + bstack1ll11_opy_ (u"ࠣࠤᆫ"))
            return
        if len(bstack1lll11llll1_opy_) > 1:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆬ") + str(kwargs) + bstack1ll11_opy_ (u"ࠥࠦᆭ"))
        bstack1lll11l11l1_opy_, bstack1lll1lll1ll_opy_ = bstack1lll11llll1_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆮ") + str(kwargs) + bstack1ll11_opy_ (u"ࠧࠨᆯ"))
            return
        return driver