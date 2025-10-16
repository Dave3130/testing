# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1lll11ll1l1_opy_,
    bstack1111111l11_opy_,
    bstack1llll11l1l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l11_opy_ import bstack1lll1l1l111_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1l11l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11l111l_opy_(bstack1lll1l1l111_opy_):
    bstack1llll111111_opy_ = bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᅞ")
    bstack1llll1111ll_opy_ = bstack1lllll1_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅟ")
    bstack1lll1l111ll_opy_ = bstack1lllll1_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅠ")
    bstack1lll1lll111_opy_ = bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅡ")
    bstack1lll1l11ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᅢ")
    bstack1llll11llll_opy_ = bstack1lllll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᅣ")
    bstack1llll111l11_opy_ = bstack1lllll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᅤ")
    bstack1lll1ll11ll_opy_ = bstack1lllll1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᅥ")
    def __init__(self):
        super().__init__(bstack1lll1ll1lll_opy_=self.bstack1llll111111_opy_, frameworks=[bstack1lllll1ll11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.BEFORE_EACH, bstack1llll1l11l1_opy_.POST), self.bstack1lll11l1lll_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11ll111_opy_ = self.bstack1lll11lll1l_opy_(instance.context)
        if not bstack1lll11ll111_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᅦ") + str(bstack1lllll111ll_opy_) + bstack1lllll1_opy_ (u"ࠥࠦᅧ"))
        f.bstack1lllll1l11l_opy_(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, bstack1lll11ll111_opy_)
        bstack1lll11l1ll1_opy_ = self.bstack1lll11lll1l_opy_(instance.context, bstack1lll111ll1l_opy_=False)
        f.bstack1lllll1l11l_opy_(instance, bstack1lll11l111l_opy_.bstack1lll1l111ll_opy_, bstack1lll11l1ll1_opy_)
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll111l11_opy_, False):
            self.__1lll111ll11_opy_(f,instance,bstack1lllll111ll_opy_)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll111l11_opy_, False):
            self.__1lll111ll11_opy_(f, instance, bstack1lllll111ll_opy_)
        if not f.get_state(instance, bstack1lll11l111l_opy_.bstack1lll1ll11ll_opy_, False):
            self.__1lll11l1l1l_opy_(f, instance, bstack1lllll111ll_opy_)
    def bstack1lll111llll_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11l1111_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11l111l_opy_.bstack1lll1ll11ll_opy_, False):
            return
        driver.execute_script(
            bstack1lllll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᅨ").format(
                json.dumps(
                    {
                        bstack1lllll1_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅩ"): bstack1lllll1_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅪ"),
                        bstack1lllll1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅫ"): {bstack1lllll1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᅬ"): result},
                    }
                )
            )
        )
        f.bstack1lllll1l11l_opy_(instance, bstack1lll11l111l_opy_.bstack1lll1ll11ll_opy_, True)
    def bstack1lll11lll1l_opy_(self, context: bstack1llll11l1l1_opy_, bstack1lll111ll1l_opy_= True):
        if bstack1lll111ll1l_opy_:
            bstack1lll11ll111_opy_ = self.bstack1lll1ll111l_opy_(context, reverse=True)
        else:
            bstack1lll11ll111_opy_ = self.bstack1lll1l1ll1l_opy_(context, reverse=True)
        return [f for f in bstack1lll11ll111_opy_ if f[1].state != bstack1llll1ll1ll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack111l1l1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1lll11l1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᅭ")).get(bstack1lllll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᅮ")):
            bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
            if not bstack1lll11ll111_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅯ") + str(bstack1lllll111ll_opy_) + bstack1lllll1_opy_ (u"ࠧࠨᅰ"))
                return
            driver = bstack1lll11ll111_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1ll1111_opy_, None)
            if not status:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅱ") + str(bstack1lllll111ll_opy_) + bstack1lllll1_opy_ (u"ࠢࠣᅲ"))
                return
            bstack1llll11ll1l_opy_ = {bstack1lllll1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᅳ"): status.lower()}
            bstack1llll111ll1_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1llll_opy_, None)
            if status.lower() == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᅴ") and bstack1llll111ll1_opy_ is not None:
                bstack1llll11ll1l_opy_[bstack1lllll1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᅵ")] = bstack1llll111ll1_opy_[0][bstack1lllll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᅶ")][0] if isinstance(bstack1llll111ll1_opy_, list) else str(bstack1llll111ll1_opy_)
            driver.execute_script(
                bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᅷ").format(
                    json.dumps(
                        {
                            bstack1lllll1_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᅸ"): bstack1lllll1_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᅹ"),
                            bstack1lllll1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅺ"): bstack1llll11ll1l_opy_,
                        }
                    )
                )
            )
            f.bstack1lllll1l11l_opy_(instance, bstack1lll11l111l_opy_.bstack1lll1ll11ll_opy_, True)
    @measure(event_name=EVENTS.bstack11111lll1l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1lll111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᅻ")).get(bstack1lllll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᅼ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11l1l11_opy_, None)
            if not test_name:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᅽ"))
                return
            bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
            if not bstack1lll11ll111_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅾ") + str(bstack1lllll111ll_opy_) + bstack1lllll1_opy_ (u"ࠨࠢᅿ"))
                return
            for bstack1lll11l11ll_opy_, bstack1lll11llll1_opy_ in bstack1lll11ll111_opy_:
                if not bstack1lllll1ll11_opy_.bstack1lll11l1111_opy_(bstack1lll11llll1_opy_):
                    continue
                driver = bstack1lll11l11ll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1lllll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆀ").format(
                        json.dumps(
                            {
                                bstack1lllll1_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆁ"): bstack1lllll1_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᆂ"),
                                bstack1lllll1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆃ"): {bstack1lllll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆄ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1lllll1l11l_opy_(instance, bstack1lll11l111l_opy_.bstack1llll111l11_opy_, True)
    def bstack1lll1llll1l_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        bstack1lll11ll111_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])]
        if not bstack1lll11ll111_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆅ"))
            return
        if not bstack1lll1l1l11l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᆆ"))
            return
        for bstack1lll111lll1_opy_ in bstack1lll11ll111_opy_:
            driver = bstack1lll111lll1_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1lllll1_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᆇ") + str(timestamp)
            driver.execute_script(
                bstack1lllll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆈ").format(
                    json.dumps(
                        {
                            bstack1lllll1_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆉ"): bstack1lllll1_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᆊ"),
                            bstack1lllll1_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆋ"): {
                                bstack1lllll1_opy_ (u"ࠧࡺࡹࡱࡧࠥᆌ"): bstack1lllll1_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᆍ"),
                                bstack1lllll1_opy_ (u"ࠢࡥࡣࡷࡥࠧᆎ"): data,
                                bstack1lllll1_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᆏ"): bstack1lllll1_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᆐ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1ll1ll1_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        keys = [
            bstack1lll11l111l_opy_.bstack1llll1111ll_opy_,
            bstack1lll11l111l_opy_.bstack1lll1l111ll_opy_,
        ]
        bstack1lll11ll111_opy_ = []
        for key in keys:
            bstack1lll11ll111_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11ll111_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧ࡮ࡺࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆑ"))
            return
        if f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll11llll_opy_, False):
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡉࡂࡕࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡧࡷ࡫ࡡࡵࡧࡧࠦᆒ"))
            return
        self.bstack1llll1lllll_opy_()
        bstack1l11llll11_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1111111ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll1l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1llllll_opy_)
        req.test_framework_state = bstack1lllll111ll_opy_[0].name
        req.test_hook_state = bstack1lllll111ll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        for bstack1lll11l11ll_opy_, driver in bstack1lll11ll111_opy_:
            try:
                webdriver = bstack1lll11l11ll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠧ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠤ࠭ࡸࡥࡧࡧࡵࡩࡳࡩࡥࠡࡧࡻࡴ࡮ࡸࡥࡥࠫࠥᆓ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᆔ")
                    if bstack1lllll1ll11_opy_.get_state(driver, bstack1lllll1ll11_opy_.bstack1lll11ll1ll_opy_, False)
                    else bstack1lllll1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᆕ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll1ll11_opy_.get_state(driver, bstack1lllll1ll11_opy_.bstack1lll1l111l1_opy_, bstack1lllll1_opy_ (u"ࠣࠤᆖ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll1ll11_opy_.get_state(driver, bstack1lllll1ll11_opy_.bstack1llll1l1l11_opy_, bstack1lllll1_opy_ (u"ࠤࠥᆗ"))
                caps = None
                if hasattr(webdriver, bstack1lllll1_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᆘ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥࡪࡩࡳࡧࡦࡸࡱࡿࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠳ࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᆙ"))
                    except Exception as e:
                        self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠻ࠢࠥᆚ") + str(e) + bstack1lllll1_opy_ (u"ࠨࠢᆛ"))
                try:
                    bstack1lll11ll11l_opy_ = json.dumps(caps).encode(bstack1lllll1_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆜ")) if caps else bstack1lll11lll11_opy_ (u"ࠣࡽࢀࠦᆝ")
                    req.capabilities = bstack1lll11ll11l_opy_
                except Exception as e:
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡪࡩࡹࡥࡣࡣࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤࡸ࡫ࡲࡪࡣ࡯࡭ࡿ࡫ࠠࡤࡣࡳࡷࠥ࡬࡯ࡳࠢࡵࡩࡶࡻࡥࡴࡶ࠽ࠤࠧᆞ") + str(e) + bstack1lllll1_opy_ (u"ࠥࠦᆟ"))
            except Exception as e:
                self.logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡶࡨࡱ࠿ࠦࠢᆠ") + str(str(e)) + bstack1lllll1_opy_ (u"ࠧࠨᆡ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1llll1l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1lll1l1l11l_opy_() and len(bstack1lll11ll111_opy_) == 0:
            bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1lll1l111ll_opy_, [])
        if not bstack1lll11ll111_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆢ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠢࠣᆣ"))
            return {}
        if len(bstack1lll11ll111_opy_) > 1:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆤ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠤࠥᆥ"))
            return {}
        bstack1lll11l11ll_opy_, bstack1lll1ll11l1_opy_ = bstack1lll11ll111_opy_[0]
        driver = bstack1lll11l11ll_opy_()
        if not driver:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆦ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠦࠧᆧ"))
            return {}
        capabilities = f.get_state(bstack1lll1ll11l1_opy_, bstack1lllll1ll11_opy_.bstack1llll11l111_opy_)
        if not capabilities:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆨ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠨࠢᆩ"))
            return {}
        return capabilities.get(bstack1lllll1_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧᆪ"), {})
    def bstack1llll11lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1lll1l1l11l_opy_() and len(bstack1lll11ll111_opy_) == 0:
            bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1lll1l111ll_opy_, [])
        if not bstack1lll11ll111_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆫ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠤࠥᆬ"))
            return
        if len(bstack1lll11ll111_opy_) > 1:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆭ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠦࠧᆮ"))
        bstack1lll11l11ll_opy_, bstack1lll1ll11l1_opy_ = bstack1lll11ll111_opy_[0]
        driver = bstack1lll11l11ll_opy_()
        if not driver:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆯ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠨࠢᆰ"))
            return
        return driver